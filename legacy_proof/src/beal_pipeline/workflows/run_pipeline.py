import os, time, random
from beal_pipeline.config import load_config
from beal_pipeline.io.loader import load_instances
from beal_pipeline.io.writer import write_table, write_json
from beal_pipeline.core.normalize import normalize_row
from beal_pipeline.core.congruences import quick_congruence_filters
from beal_pipeline.core.lte import lte_check
from beal_pipeline.core.zsigmondy import zsigmondy_barrier
from beal_pipeline.core.pinch_height_radical import pinch_metrics
from beal_pipeline.core.beal_check import beal_identity_holds
from beal_pipeline.utils.hashing import hash_obj
from beal_pipeline.utils.tablegen import summary_table
from beal_pipeline.utils.logging import get_logger

def run_pipeline(config_path: str):
    cfg = load_config(config_path)
    log = get_logger(level=cfg.get("log_level","INFO"))
    seed = int(cfg.get("seed", 42))
    random.seed(seed)

    input_csv = cfg["input_csv"]
    out_dir = cfg.get("output_dir","data/output")
    os.makedirs(out_dir, exist_ok=True)

    df = load_instances(input_csv)
    rows = []
    t0 = time.time()

    for row in df.itertuples(index=False):
        norm = normalize_row(row)
        if norm["status"] != "ok":
            rows.append({"id":row.id, "status":"discard", "reason":norm["reason"]})
            continue

        x,y,z,a,b,c = norm["x"],norm["y"],norm["z"],norm["a"],norm["b"],norm["c"]

        # Congruências
        cong = quick_congruence_filters(
            x,y,z,a,b,c,
            mods=tuple(cfg.get("congruence_mods", (2,3,4,5,8,9,11)))
        )
        if cong["discard"]:
            rows.append({"id":row.id,"status":"discard","reason":cong["reason"]})
            continue

        # LTE
        lte = lte_check(x,y,a,b)
        # Se quisermos um critério de descarte simples baseado em LTE, poderíamos:
        # if lte["contradiction"]:
        #     rows.append({"id":row.id,"status":"discard","reason":"lte_contradiction"})
        #     continue

        # Zsigmondy (para n = max(a,b))
        zsig = zsigmondy_barrier(x,y,max(a,b), plus=False)
        if zsig.get("exception") and zsig.get("reason") not in {"primitive_prime_exists"}:
            # Exceções clássicas ou falta de primo novo → descartar
            rows.append({"id":row.id,"status":"discard","reason":f"zsigmondy_{zsig['reason']}"})
            continue

        # Pinça
        pm = cfg.get("pinch", {})
        pinch = pinch_metrics(
            x,y,z,a,b,c,
            max_ratio=pm.get("max_ratio", None),
            enable=pm.get("enable", True)
        )
        if pinch["discard"]:
            rows.append({"id":row.id,"status":"discard","reason":pinch["reason"],"H":pinch["H"],"R":pinch["R"],"ratio":pinch["ratio"]})
            continue

        # Identidade Beal
        holds = beal_identity_holds(x,y,z,a,b,c)
        status = "holds" if holds else "passed_filters"

        rows.append({
            "id":row.id,
            "status":status,
            "reason":None if holds else "filters_ok",
            "lte_notes":";".join(lte["notes"]),
            "zsig_reason":zsig["reason"],
            "H":pinch["H"],
            "R":pinch["R"],
            "ratio":pinch["ratio"]
        })

    elapsed = round(time.time()-t0, 3)
    table = summary_table(rows)

    tables_dir = os.path.join(out_dir,"tables")
    chk_dir = os.path.join(out_dir,"checkpoints")
    os.makedirs(tables_dir, exist_ok=True)
    os.makedirs(chk_dir, exist_ok=True)

    path_csv = os.path.join(tables_dir,"summary.csv")
    write_table(table, path_csv)

    manifest = {
        "config": cfg,
        "rows_count": len(rows),
        "rows_hash": hash_obj(rows),
        "input_csv": input_csv,
        "output_summary": path_csv,
        "elapsed_seconds": elapsed,
        "seed": seed,
    }
    write_json(manifest, os.path.join(chk_dir,"manifest.json"))
    log.info(f"Pipeline done in {elapsed}s | rows={len(rows)} | hash={manifest['rows_hash']}")
    return path_csv
