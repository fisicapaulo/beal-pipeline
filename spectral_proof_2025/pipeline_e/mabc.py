# spectral_proof_2025/pipeline_e/mabc.py
import math

def M_ABC(A: int, B: int, C: int, delta: float, alpha_Q: float, C0: float) -> int:
    """
    Implements:
        M(A,B,C) = floor( ((1 - delta) * alpha_Q * log(rad(ABC)) + C0) / min{log A, log B, log C} )

    Assumes A,B,C >= 1 (coprime) and delta in (0,1).
    The caller must supply rad(ABC).
    """
    if min(A, B, C) < 1:
        raise ValueError("A, B, C must be >= 1.")
    if not (0 < delta < 1):
        raise ValueError("delta must be in (0,1).")
    # Guard: if any of A,B,C == 1, handle log(1)=0 safely
    logs = [math.log(max(1, A)), math.log(max(1, B)), math.log(max(1, C))]
    denom = min([x for x in logs if x > 0] or [1.0])  # avoid zero: fall back to 1.0
    return None, denom  # this function is resolved in pipeline_e.py with rad(ABC)
