# spectral_proof_2025/pipeline_e/congruences.py
def pow_mod(a: int, e: int, m: int) -> int:
    return pow(a % m, e, m)

def basic_congruence_filters(A: int, B: int, C: int, x: int, y: int, z: int) -> bool:
    """
    Return True if the triple (A,B,C;x,y,z) survives basic modular filters
    mod m in {3,4,5,8,9,11} (optionally we can add 7,13 later).
    If False, it is eliminated (contradiction).
    """
    mods = [3,4,5,8,9,11]
    for m in mods:
        lhs = (pow_mod(A, x, m) + pow_mod(B, y, m)) % m
        rhs = pow_mod(C, z, m)
        if lhs != rhs:
            return False  # eliminated by modular inconsistency
    return True
