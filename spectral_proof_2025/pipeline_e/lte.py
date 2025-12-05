# spectral_proof_2025/pipeline_e/lte.py
from math import log2
from .valuations import p_adic_valuation

def lte_plus(A: int, B: int, n: int, p: int) -> int:
    """
    LTE for A^n + B^n when n is odd, p >=3, p | (A+B), p not | AB:
    v_p(A^n + B^n) = v_p(A+B) + v_p(n).
    For p=2, special cases are needed; handled separately in lte_two().
    """
    if p == 2:
        return lte_two(A, B, n, plus=True)
    if n % 2 == 0:
        return 0
    if (A + B) % p != 0:
        return 0
    if A % p == 0 or B % p == 0:
        return 0
    return p_adic_valuation(A + B, p) + p_adic_valuation(n, p)

def lte_minus(A: int, B: int, n: int, p: int) -> int:
    """
    LTE for A^n - B^n when p >=3, p | (A-B), p not | AB:
    v_p(A^n - B^n) = v_p(A-B) + v_p(n).
    For p=2, special cases handled in lte_two().
    """
    if p == 2:
        return lte_two(A, B, n, plus=False)
    if (A - B) % p != 0:
        return 0
    if A % p == 0 or B % p == 0:
        return 0
    return p_adic_valuation(A - B, p) + p_adic_valuation(n, p)

def lte_two(A: int, B: int, n: int, plus: bool) -> int:
    """
    Very basic handling for p=2; enough to produce contradictions when possible.
    We can refine later (cases mod 8,16). Here, return a lower bound heuristic.
    """
    # If both A,B odd and plus with n odd, then 2 | (A^n + B^n).
    if A % 2 == 1 and B % 2 == 1 and plus and (n % 2 == 1):
        return 1  # v_2 >= 1 (can be more with finer analysis)
    # If A,B odd and minus with A != B, then A^n - B^n is even if A-B even.
    if A % 2 == 1 and B % 2 == 1 and not plus and ((A - B) % 2 == 0):
        return 1
    return 0
