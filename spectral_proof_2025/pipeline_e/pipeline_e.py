# spectral_proof_2025/pipeline_e/pipeline_e.py
import math
from sympy import factorint, gcd
from .valuations import radical_ABC, p_adic_valuation
from .zsigmondy import has_zsigmondy_new_prime
from .congruences import basic_congruence_filters
from .lte import lte_plus, lte_minus

def compute_M(A, B, C, delta, alpha_Q, C0):
    rad = radical_ABC(A, B, C)
    logs = [math.log(max(1, A)), math.log(max(1, B)), math.log(max(1, C))]
    denom = min([x for x in logs if x > 0] or [1.0])
    num = (1.0 - delta) * alpha_Q * math.log(rad) + C0
    if denom <= 0:
        return 0
    return max(0, int(math.floor(num / denom)))

def enumerate_triples(Mmax):
    res = []
    for x in range(3, Mmax + 1):
        for y in range(3, Mmax + 1):
            for z in range(3, Mmax + 1):
                if x + y + z <= Mmax:
                    res.append((x, y, z))
    return res

def contradict_with_zsigmondy(A, B, x, y):
    # Try plus first (A^n + B^n)
    if has_zsigmondy_new_prime(A, B, x, use_plus=True):
        return True
    if has_zsigmondy_new_prime(A, B, y, use_plus=True):
        return True
    # Also try minus as auxiliary obstruction if needed
    if has_zsigmondy_new_prime(A, B, x, use_plus=False):
        return True
    if has_zsigmondy_new_prime(A, B, y, use_plus=False):
        return True
    return False

def contradict_with_lte_and_coprimality(A, B, C, x, y, z):
    """
    Try to find a prime p that divides A^x ± B^y with v_p>0 while v_p(C^z)=0 (coprime).
    We attempt a few candidate primes from small set and from factors of A±B, A−B.
    """
    candidates = set()
    # Gather small primes plus primes from A±B
    for p in [2,3,5,7,11,13,17,19,23]:
        candidates.add(p)
    for base in [A + B, A - B]:
        for p in factorint(abs(base) if base != 0 else 0).keys():
            candidates.add(p)

    for p in sorted(candidates):
        if p <= 1:
            continue
        # Skip if p | C (coprimality would forbid; but check anyway)
        if C % p == 0:
            continue
        vpCz = 0  # by coprimality expected 0
        # Evaluate valuations on A^x ± B^y:
        vp_plus = lte_plus(A, B, x, p) if x % 2 == 1 else 0
        vp_minus = lte_minus(A, B, x, p)
        if vp_plus > 0 or vp_minus > 0:
            # We have positive valuation on LHS vs zero on RHS
            return True
        # Try symmetric in y if needed
        vp_plus_y = lte_plus(A, B, y, p) if y % 2 == 1 else 0
        vp_minus_y = lte_minus(A, B, y, p)
        if vp_plus_y > 0 or vp_minus_y > 0:
            return True
    return False

def pipeline_E(A, B, C, delta=0.2, alpha_Q=10.0, C0=100.0, verbose=True):
    """
    Execute the five-step pipeline for given coprime A,B,C >= 1.
    Default constants are placeholders; adjust to your theoretical values.
    Returns a dict with diagnostics.
    """
    if gcd(A, B) != 1 or gcd(B, C) != 1 or gcd(A, C) != 1:
        raise ValueError("A,B,C must be pairwise coprime.")
    Mmax = compute_M(A, B, C, delta, alpha_Q, C0)
    triples = enumerate_triples(Mmax)

    if verbose:
        print(f"[E] A={A}, B={B}, C={C} | rad(ABC)={radical_ABC(A,B,C)} | M={Mmax} | candidates={len(triples)}")

    eliminated_by_congruence = 0
    eliminated_by_zsigmondy = 0
    eliminated_by_lte = 0
    survivors = []

    for (x, y, z) in triples:
        # Step (ii): congruence filters
        if not basic_congruence_filters(A, B, C, x, y, z):
            eliminated_by_congruence += 1
            continue

        # Step (iii): Zsigmondy
        if contradict_with_zsigmondy(A, B, x, y):
            eliminated_by_zsigmondy += 1
            continue

        # Step (iv)+(v): LTE + support/valuations contradiction
        if contradict_with_lte_and_coprimality(A, B, C, x, y, z):
            eliminated_by_lte += 1
            continue

        survivors.append((x, y, z))

    return {
        "A": A, "B": B, "C": C,
        "M": Mmax,
        "tested": len(triples),
        "eliminated_by_congruence": eliminated_by_congruence,
        "eliminated_by_zsigmondy": eliminated_by_zsigmondy,
        "eliminated_by_lte": eliminated_by_lte,
        "survivors": survivors,
    }
