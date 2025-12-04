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

O projeto está organizado em duas fases distintas de desenvolvimento:

### 1. [`spectral_proof_2025/`](./spectral_proof_2025) (Abordagem Atual)
Contém a implementação numérica da prova teórica apresentada no artigo *"Coerção Espectral e Contração Arakeloviana"*.

- `core/`: Definições formais de métricas (Altura Logarítmica, Radical Prímico, Primitividade).
- `simulation/`: "Stress Test" que busca contraexemplos em milhões de permutações de bases e expoentes.
- `visualization/`: Scripts para gerar evidências visuais do gap `δ > 0` e do descolamento entre altura e radical.

### 2. [`legacy_proof/`](./legacy_proof) (Arquivado)
Contém experimentos, códigos e rascunhos das primeiras iterações desta pesquisa. Mantido para fins de registro histórico.

---

## 🚀 Como Executar (Spectral Proof)

Para reproduzir os testes da abordagem espectral em sua máquina local:

### Pré-requisitos

```bash
pip install sympy pandas seaborn matplotlib
```

### 🔬 Rodando o Stress Test

Para verificar a robustez da desigualdade arakeloviana contra milhões de triplas quase-solução:

```bash
cd spectral_proof_2025
python -m simulation.inequality_test
```

### 📊 Visualização da Prova

Para plotar o gráfico de dispersão (Height vs Radical) que evidencia a "Região Proibida":

```bash
cd spectral_proof_2025
python -m visualization.height_vs_radical
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

<div align="center">

**Autor:** Paulo Vieira • **Contato:** libreeducacional@gmail.com

Defendendo a Ciência Aberta: código auditável e reprodutível.

</div>
````

- Licença: MIT (arquivo `LICENSE`)
- Autor: Paulo Vieira
- Contato: libreeducacional@gmail.com
- Status do repositório: Pesquisa ativa, com ênfase em auditoria e reprodutibilidade
````
