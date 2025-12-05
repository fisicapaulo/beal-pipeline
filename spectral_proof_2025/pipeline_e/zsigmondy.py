# spectral_proof_2025/pipeline_e/zsigmondy.py
from sympy import gcd, factorint

def has_zsigmondy_new_prime(A: int, B: int, n: int, use_plus: bool = True) -> bool:
    """
    Heuristic/practical check:
    - Compute N = A^n ± B^n and its prime factors.
    - Check if there exists a prime p dividing N that does not divide A*B.
    This serves as a computational proxy for 'new prime' in Zsigmondy.
    For large exponents this can be expensive; here, intended for finite window.
    """
    if n < 3:
        return False
    if gcd(A, B) != 1:
        return False
    val = pow(A, n) + pow(B, n) if use_plus else pow(A, n) - pow(B, n)
    val = abs(val)
    if val == 0:
        return False
    fac = factorint(val)  # {p: e}
    for p in fac:
        if A % p != 0 and B % p != 0:
            return True
    return False
