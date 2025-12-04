# spectral_proof_2025/visualization/__init__.py

"""
Visualization Module: Evidências Gráficas.

Este submódulo gera as visualizações que demonstram o descolamento
entre a Altura h(P) e o log(rad(ABC)).
"""

from .height_vs_radical import plot_inequality_landscape

__all__ = ['plot_inequality_landscape']