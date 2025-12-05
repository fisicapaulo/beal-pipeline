<div align="center">

# Beal Pipeline: Unified Foundational Theory Verification
### Coerção Espectral e Contração Arakeloviana

<p>
  <a href="#-como-executar-spectral-proof">
    <img src="https://img.shields.io/badge/Execute-Stress_Test-green?style=for-the-badge&logo=python" alt="Execute Test" />
  </a>
  <a href="#-visualização-da-prova">
    <img src="https://img.shields.io/badge/View-Proof_Plot-blue?style=for-the-badge&logo=matplotlib" alt="View Plot" />
  </a>
  <a href="https://colab.research.google.com/">
    <img src="https://img.shields.io/badge/Open_in-Colab-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab" />
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Active_Research-success" alt="Status" />
  <img src="https://img.shields.io/badge/Theory-Spectral_Arakelov-blueviolet" alt="Theory" />
  <img src="https://img.shields.io/badge/Language-Python_3.8+-yellow" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License" />
</p>

</div>

---

## 📜 Sobre o Projeto

Este repositório contém os pipelines computacionais e a documentação associada à pesquisa de **Paulo Vieira** sobre a **Conjectura de Beal Generalizada**. O projeto documenta a evolução da investigação, culminando na **Abordagem Espectral-Arakeloviana (2025)**, que propõe uma prova baseada na rigidez geométrica e na coerção de operadores elípticos.

A tese central validada por este código é a desigualdade de contração de alturas:

```math
h(P) \le (1-\delta)\log\text{rad}(ABC) + C_{\mathrm{Global}}
```

---

## 📂 Estrutura do Repositório

O projeto está organizado em duas frentes:

### 1) `spectral_proof_2025/` (Abordagem Atual)
Implementação numérica da prova teórica apresentada no artigo “Coerção Espectral e Contração Arakeloviana”.

- `core/` — métricas formais (Altura Logarítmica, Radical Prímico, Primitividade).
- `simulation/` — “stress test” que busca contraexemplos em grandes amostras.
- `visualization/` — scripts para evidenciar o gap δ > 0 e o descolamento Altura vs. Radical.
- `pipeline_e/` — Apêndice E: módulo consolidado com checagens aritméticas clássicas (congruências, LTE, Zsigmondy, valuations, M(A,B,C)).
- `run_pipeline_e.py` — ponto de entrada para executar o Pipeline E end-to-end.

### 2) `legacy_proof/` (Arquivado)
Iterações anteriores (rascunhos, experimentos e testes unitários legados) preservadas para histórico e auditoria.

---

## 🚀 Como Executar (Spectral Proof)

Abaixo um fluxo mínimo para reproduzir resultados localmente.

### Pré-requisitos

Instale as dependências essenciais (ajuste conforme seu ambiente):
```bash
python -m pip install --upgrade pip
pip install sympy pandas seaborn matplotlib
```

Se existir um arquivo `requirements.txt`, prefira:
```bash
pip install -r requirements.txt
```

---

### 🔬 Stress Test (Abordagem Espectral)

Executa a verificação robusta da desigualdade arakeloviana em múltiplas triplas quase-solução:

```bash
python -m spectral_proof_2025.simulation.stress_test
```

---

### 📊 Visualização da Prova

Gera gráfico de dispersão (Height vs. Radical) destacando a “Região Proibida”:

```bash
python -m spectral_proof_2025.visualization.plot_proof
```

---

## 📎 Apêndice E — Pipeline E (Verificações Aritméticas Clássicas)

O Apêndice E reúne rotinas clássicas que complementam a abordagem espectral, permitindo inspeções estruturadas em casos-modelo e validações cruzadas.

- Módulos principais:
  - `pipeline_e/congruences.py` — checagens modulares e congruências estruturais.
  - `pipeline_e/lte.py` — Lifting The Exponent (LTE).
  - `pipeline_e/zsigmondy.py` — existência de primos de Zsigmondy em progressões relevantes.
  - `pipeline_e/valuations.py` — valuations p-ádicas e controle fino de expoentes.
  - `pipeline_e/mabc.py` — funções auxiliares M(A,B,C) e primitividade.
  - `pipeline_e/pipeline_e.py` — orquestração das rotinas acima.

### ▶ Execução rápida do Pipeline E

Use o entrypoint preparado:
```bash
python spectral_proof_2025/run_pipeline_e.py
```

Alternativa via módulo:
```bash
python -m spectral_proof_2025.run_pipeline_e
```

Saídas típicas:
- Relatórios de congruências e valuations por tríplice testada.
- Indicadores de primitividade e sinais de Zsigmondy/LTE para os casos varridos.
- Resumo final com estatísticas da varredura.

Dica: ajuste parâmetros e amostras diretamente em `pipeline_e/pipeline_e.py` e/ou `mabc.py`.

---

## 🧪 Reprodutibilidade e Testes

- Testes legados em `legacy_proof/tests/` cobrem congruências, LTE, normalização e Zsigmondy das versões anteriores.
- Para novas rotinas do Apêndice E, recomenda-se adicionar testes em `spectral_proof_2025/pipeline_e/` seguindo o padrão PyTest.

Execução sugerida (se houver PyTest):
```bash
pytest -q
```

---

## 📄 Citação

Este código serve de suporte computacional para o artigo teórico. Ao utilizar ou referenciar este trabalho, favor citar:

> Vieira, Paulo (2025). Coerção Espectral e Contração Arakeloviana: Uma Prova Autocontida da Conjectura de Beal Generalizada. [Preprint]

```bibtex
@misc{Vieira2025Beal,
  author = {Vieira, Paulo},
  title = {Coerção Espectral e Contração Arakeloviana: Uma Prova Autocontida da Conjectura de Beal Generalizada},
  year = {2025},
  note = {GitHub Repository: https://github.com/fisicapaulo/beal-pipeline}
}
```

---

## 🔑 Licença e Contato

- Licença: MIT (veja o arquivo `LICENSE`)
- Autor: Paulo Vieira
- Contato: libreeducacional@gmail.com
- Status do repositório: Pesquisa ativa, com ênfase em auditoria e reprodutibilidade

---

<div align="center">

Defendendo a Ciência Aberta: código auditável e reprodutível.

</div>
```
