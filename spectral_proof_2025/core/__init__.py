# spectral_proof_2025/core/__init__.py

"""
Core Module: Métricas Aritméticas e Espectrais.

Este submódulo contém as definições fundamentais de altura,
radical e primitividade, além do teste de delta espectral.
"""

from .metrics import (
    get_radical,
    logarithmic_height,
    check_primitiveness,
    spectral_delta_test
)

# Define o que é exportado quando se usa 'from core import *'
__all__ = [
    'get_radical',
    'logarithmic_height',
    'check_primitiveness',
    'spectral_delta_test'
]