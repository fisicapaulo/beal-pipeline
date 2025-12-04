# -*- coding: utf-8 -*-
"""
Módulo Core: Métricas Arakelovianas e Aritméticas
Autor: Paulo Vieira
Contexto: Teoria Fundacional Unificada / Conjectura de Beal
"""

import math
from sympy.ntheory import factorint
from functools import reduce

def get_radical(n):
    """
    Calcula o radical de n (produto dos primos distintos).
    rad(n) = product(p_i).
    """
    if n == 0: return 0
    if n == 1: return 1
    factors = factorint(abs(n))
    return reduce(lambda x, y: x * y, factors.keys())

def logarithmic_height(A, x, B, y, C, z):
    """
    Calcula a altura logarítmica normalizada h(P).
    h(P) ~ max(x log|A|, y log|B|, z log|C|)
    """
    h_A = x * math.log(abs(A)) if A != 0 else 0
    h_B = y * math.log(abs(B)) if B != 0 else 0
    h_C = z * math.log(abs(C)) if C != 0 else 0
    return max(h_A, h_B, h_C)

def check_primitiveness(A, B, C):
    """
    Verifica se a tripla é primitiva: gcd(A, B, C) == 1.
    """
    return math.gcd(A, math.gcd(B, C)) == 1

def spectral_delta_test(A, x, B, y, C, z, C_global=1.0):
    """
    Testa a inequação global para uma tripla dada e retorna o delta empírico.
    Inequação: h(P) <= (1 - delta) * log(rad(ABC)) + C_global
    
    Retorna:
    - delta_empirico: O valor de delta necessário para satisfazer a equação.
    - is_violation: True se delta for negativo (o que contradiria a teoria para C calibrado).
    """
    h_P = logarithmic_height(A, x, B, y, C, z)
    ABC = A * B * C
    log_rad = math.log(get_radical(ABC))
    
    # h(P) - C_global <= (1 - delta) * log_rad
    # (h(P) - C_global) / log_rad <= 1 - delta
    # delta <= 1 - (h(P) - C_global) / log_rad
    
    if log_rad == 0: return 0, False # Evita divisão por zero
    
    ratio = (h_P - C_global) / log_rad
    delta_empirico = 1.0 - ratio
    
    return delta_empirico, delta_empirico < 0