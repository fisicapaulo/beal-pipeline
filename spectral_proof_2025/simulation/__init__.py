# spectral_proof_2025/simulation/__init__.py

"""
Simulation Module: Testes de Estresse e Geração de Dados.

Este submódulo é responsável por gerar milhões de triplas (A, B, C)
para tentar falsear a desigualdade arakeloviana.
"""

from .inequality_test import generate_quasi_beal

__all__ = ['generate_quasi_beal']