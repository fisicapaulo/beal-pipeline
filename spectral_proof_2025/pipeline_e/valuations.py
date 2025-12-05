# spectral_proof_2025/pipeline_e/valuations.py
from sympy import factorint

def p_adic_valuation(n: int, p: int) -> int:
    """Return v_p(n), p-adic valuation for integer n >= 1."""
    if n == 0:
        raise ValueError("v_p(0) is infinite; not supported.")
    if p <= 1:
        raise ValueError("p must be a prime >= 2.")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def radical(n: int) -> int:
    """Return rad(n): product of distinct prime divisors of n (n>=1)."""
    if n < 1:
        raise ValueError("n must be >= 1.")
    if n == 1:
        return 1
    fac = factorint(n)  # dict {p: e}
    rad = 1
    for p in fac.keys():
        rad *= p
    return rad

def radical_ABC(A: int, B: int, C: int) -> int:
    """Return rad(ABC)."""
    return radical(abs(A * B * C))
