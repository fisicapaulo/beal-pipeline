from sympy import factorint
from typing import Dict, Optional

def radical(n:int) -> int:
    r = 1
    for p in factorint(abs(n)).keys():
        r *= p
    return r

def pinch_metrics(x:int,y:int,z:int,a:int,b:int,c:int, max_ratio: Optional[float]=None, enable: bool=True) -> Dict:
    H = max(abs(x)**a, abs(y)**b, abs(z)**c)
    R = radical(x) * radical(y) * radical(z)
    ratio = H / max(R, 1)
    res = {"H": H, "R": R, "ratio": ratio, "discard": False, "reason": None}
    if enable and (max_ratio is not None):
        if ratio > max_ratio:
            res["discard"] = True
            res["reason"] = f"pinch_ratio_exceeds_{max_ratio}"
    return res
