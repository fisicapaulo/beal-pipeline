````markdown
# beal-pipeline

![Run Status](https://img.shields.io/badge/run--status-OK-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellow)

Pipeline reprodutível para triagem computacional de instâncias estilo Beal, com documentação unificada e duas frentes metodológicas: a Prova Espectral–Arakeloviana (atual) e a Prova Legado (histórica). Mantém botões/status, instruções objetivas e foco em ciência aberta.

---

## 📚 Visão Geral

Este repositório consolida os pipelines e materiais associados à investigação sobre a Conjectura de Beal Generalizada. A fase atual enfatiza coerção espectral e montagem arakeloviana para controlar alturas, enquanto a fase legado registra experimentos anteriores para transparência.

- Núcleo matemático modular (congruências, LTE, Zsigmondy, pinça altura–radical)
- CLI em Python
- Orquestração reprodutível (config YAML, determinismo)
- Logs estruturados e hashes
- Artefatos: CSV/Markdown, checkpoints JSON/Parquet, relatórios HTML
- Testes mínimos
- Defesa explícita de ciência aberta e uso de ecossistemas Python/SageMath

---

# Beal Pipeline: Unified Foundational Theory Verification

> **Repository Status:** Active Research
> **Topic:** Diophantine Geometry, Spectral Theory, Arakelov Heights

Este repositório contém os pipelines computacionais e a documentação associada à pesquisa de Paulo Vieira sobre a **Conjectura de Beal Generalizada**. O projeto documenta a evolução da investigação, culminando na **Abordagem Espectral-Arakeloviana (2025)**, que propõe uma prova baseada na rigidez geométrica e na coerção de operadores elípticos.

## 📂 Estrutura do Repositório

O projeto está organizado em duas fases distintas de desenvolvimento:

### 1. [`spectral_proof_2025/`](./spectral_proof_2025) (Current Approach)
Esta pasta contém a implementação numérica da prova teórica apresentada no artigo *"Coerção Espectral e Contração Arakeloviana"*. Os scripts simulam o comportamento de alturas e radicais para validar a desigualdade fundamental:

$$h(P) \le (1-\delta)\log\text{rad}(ABC) + C_{\mathrm{Global}}$$

* **`core/`**: Definições formais de métricas (Altura Logarítmica, Radical Prímico, Primitividade).
* **`simulation/`**: "Stress Test" que busca contraexemplos em milhões de permutações de bases e expoentes.
* **`visualization/`**: Scripts para gerar evidências visuais do gap $\delta > 0$ e do descolamento entre altura e radical.

### 2. [`legacy_proof/`](./legacy_proof) (Archived)
Contém experimentos, códigos e rascunhos das primeiras iterações desta pesquisa. Estes arquivos são mantidos para fins de registro histórico e transparência sobre a evolução do método de prova.

---

## 🚀 Como Executar (Spectral Proof)

Para reproduzir os testes da abordagem espectral:

### Pré-requisitos
* Python 3.8+
* Bibliotecas: `sympy`, `pandas`, `seaborn`, `matplotlib`

```bash
pip install sympy pandas seaborn matplotlib

---

## ▶️ Execução Rápida

```bash
bash scripts/example_run.sh
```
Após a execução, verifique:
- `data/output/tables/summary.csv`
- `data/output/checkpoints/manifest.json`

---

## ⚙️ Configuração

Edite `config.yaml`.

Observação: se `pinch.max_ratio` estiver como string `"1e6"`, altere para número `1000000` para evitar discrepâncias de tipo.

---

## 🚀 Como Rodar a Prova Espectral

Pré-requisitos:
- Python 3.11+
- Bibliotecas: `sympy`, `pandas`, `seaborn`, `matplotlib`

Instalação de deps:
```bash
python -m pip install --upgrade pip
pip install sympy pandas seaborn matplotlib
```

Stress test:
```bash
cd spectral_proof_2025
python -m simulation.inequality_test
```

Visualizações:
```bash
cd spectral_proof_2025
python -m visualization.height_vs_radical
```

---

## 🧹 .gitignore (Recomendado)

Garanta que os artefatos não sejam versionados:
```
data/output/
data/output/**
```

---

## 📄 Citação e Referência Acadêmica

Este código dá suporte computacional à abordagem teórica. Ao utilizar ou referenciar:

> Vieira, Paulo (2025). “Coerção Espectral e Contração Arakeloviana: Uma Prova Autocontida da Conjectura de Beal Generalizada.” [Preprint/Em Submissão]

BibTeX:
```bibtex
@misc{Vieira2025Beal,
  author = {Vieira, Paulo},
  title = {Coerção Espectral e Contração Arakeloviana: Uma Prova Autocontida da Conjectura de Beal Generalizada},
  year = {2025},
  note = {GitHub Repository: https://github.com/fisicapaulo/beal-pipeline}
}
```

---

## 🤝 Agradecimentos

Gratidão à família, em especial à irmã Mônica, fundamental para a formação universitária do autor. Reconhecimento à comunidade de software científico aberto, especialmente Python e SageMath, cuja infraestrutura e ethos colaborativo permitem pesquisa transparente, reproduzível e auditável. Ciência aberta é pilar de robustez e avanço coletivo.

---

## ⚖️ Licença e Contato

- Licença: MIT (arquivo `LICENSE`)
- Autor: Paulo Vieira
- Contato: libreeducacional@gmail.com
- Status do repositório: Pesquisa ativa, com ênfase em auditoria e reprodutibilidade
````
