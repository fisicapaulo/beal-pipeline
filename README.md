# beal-pipeline

Pipeline reprodutível para triagem computacional de instâncias estilo Beal, com:
- CLI em Python
- Núcleo matemático modular (congruências, LTE, Zsigmondy, pinça altura–radical)
- Orquestração reprodutível (config YAML, determinismo)
- Logs estruturados e hashes
- Artefatos: CSV/Markdown, checkpoints JSON/Parquet, relatórios HTML
- Testes mínimos

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

## Execução
```bash
bash scripts/example_run.sh
```
Verifique `data/output/tables/summary.csv`.

## Configuração
Edite `config.yaml`.

## Licença
MIT (LICENSE).
