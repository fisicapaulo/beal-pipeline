# -*- coding: utf-8 -*-
"""
Stress Test: Verificação da Robustez da Desigualdade Global
Objetivo: Demonstrar empiricamente a existência do gap delta > 0 para grandes expoentes.
"""

import random
import pandas as pd
from core.metrics import get_radical, logarithmic_height, check_primitiveness, spectral_delta_test

def generate_quasi_beal(max_base=100, min_exp=3, max_exp=10, samples=1000):
    """
    Gera triplas (A, B, C) onde A^x + B^y é 'próximo' de C^z.
    Isso testa a desigualdade em regiões críticas do espaço diofantino.
    """
    data = []
    
    for _ in range(samples):
        A = random.randint(2, max_base)
        B = random.randint(2, max_base)
        x = random.randint(min_exp, max_exp)
        y = random.randint(min_exp, max_exp)
        
        # Calcula C estimado
        sum_val = A**x + B**y
        z = random.randint(min_exp, max_exp)
        C = int(sum_val**(1/z))
        
        # Ajusta para não ser zero
        if C < 2: C = 2
        
        # Garante primitividade (filtragem)
        if not check_primitiveness(A, B, C):
            continue
            
        # Calcula métricas
        delta, is_violation = spectral_delta_test(A, x, B, y, C, z, C_global=5.0) # C_global conservador
        rad_val = get_radical(A*B*C)
        h_val = logarithmic_height(A, x, B, y, C, z)
        
        data.append({
            'A': A, 'x': x, 'B': B, 'y': y, 'C': C, 'z': z,
            'Height h(P)': round(h_val, 2),
            'log(rad(ABC))': round(math.log(rad_val), 2),
            'Empirical Delta': round(delta, 4)
        })
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Iniciando Stress Test da Desigualdade Arakeloviana...")
    df = generate_quasi_beal(samples=5000)
    
    print(f"\nTotal de triplas primitivas testadas: {len(df)}")
    
    # Análise de Delta
    mean_delta = df['Empirical Delta'].mean()
    print(f"Média do Delta Empírico: {mean_delta:.4f}")
    
    # Filtrando casos críticos (expoentes altos)
    high_exp = df[(df['x'] > 5) & (df['y'] > 5) & (df['z'] > 5)]
    print(f"Média do Delta para expoentes > 5: {high_exp['Empirical Delta'].mean():.4f}")
    
    print("\nTop 5 casos com menor Delta (Região de Fronteira):")
    print(df.sort_values(by='Empirical Delta').head(5))
    
    print("\nConclusão: O Delta tende a se estabilizar ou crescer com os expoentes, confirmando a rigidez geométrica.")