# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
from simulation.stress_test import generate_quasi_beal
import numpy as np

def plot_inequality_landscape():
    # Gerar dados
    df = generate_quasi_beal(max_base=50, min_exp=3, max_exp=15, samples=2000)
    
    plt.figure(figsize=(12, 8))
    sns.set_style("whitegrid")
    
    # Scatter Plot
    sns.scatterplot(
        data=df, 
        x='log(rad(ABC))', 
        y='Height h(P)', 
        hue='z', 
        palette='viridis', 
        size='x',
        sizes=(20, 200),
        alpha=0.7
    )
    
    # Linha Teórica de Contradição (exemplo com delta=0.1)
    # h(P) = (1-delta) * log_rad + C
    x_vals = np.linspace(df['log(rad(ABC))'].min(), df['log(rad(ABC))'].max(), 100)
    delta_theoretical = 0.1
    c_global = 5.0
    y_vals = (1 - delta_theoretical) * x_vals + c_global
    
    plt.plot(x_vals, y_vals, color='red', linestyle='--', linewidth=2, label=r'Theoretical Bound: $1-\delta$ slope')
    
    plt.title(r'Evidência Visual da Contração: $h(P)$ vs $\log(\text{rad}(ABC))$', fontsize=16)
    plt.xlabel(r'$\log(\text{rad}(ABC))$ (Complexidade Aritmética)', fontsize=14)
    plt.ylabel(r'Altura $h(P)$ (Complexidade Geométrica)', fontsize=14)
    plt.legend(title='Expoente z')
    
    # Anotação
    plt.text(x_vals[0], y_vals[-1], r'Forbidden Region for Solutions', color='red', fontsize=12, rotation=0)
    
    plt.tight_layout()
    plt.savefig("proof_landscape.png", dpi=300)
    print("Gráfico salvo como proof_landscape.png")

if __name__ == "__main__":
    plot_inequality_landscape()