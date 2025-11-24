# beal-pipeline
![Run Status](https://img.shields.io/badge/run--status-OK-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellow)

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
Verifique `data/output/tables/summary.csv` e `data/output/checkpoints/manifest.json`.

## Configuração
Edite `config.yaml`. Observação: se `pinch.max_ratio` estiver como string `"1e6"`, você pode trocar para número `1000000` para evitar discrepâncias de tipo.

## Estrutura
```
src/beal_pipeline/        # núcleo e workflows
scripts/                  # scripts de execução
data/input/               # entradas (ex.: samples.csv)
data/output/              # saídas geradas (não versionar)
tests/                    # testes mínimos
```

## GitHub Actions (opcional)
Crie `.github/workflows/ci.yml` para rodar lint e testes em cada push/PR:
```yaml
name: CI
on:
  push:
    branches: [ "main" ]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -e .
          pip install pytest flake8
      - name: Lint
        run: flake8 src tests || true
      - name: Tests
        run: pytest -q
```

## .gitignore (recomendado)
Garanta que os artefatos não sejam versionados:
```
data/output/
data/output/**
```

## Licença
MIT (LICENSE).
