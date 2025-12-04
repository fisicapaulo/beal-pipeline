from beal_pipeline.core.congruences import quick_congruence_filters

def test_parity_mismatch():
    # simples: apenas valida retorno estruturado
    out = quick_congruence_filters(2,3,2,3,2,2)
    assert isinstance(out, dict)
