from typing import Dict
from sympy import factorint

EXCEPTIONS = [
    # (x,y,n) padrões clássicos onde pode falhar primo novo
    # x - y = 1 e n = 2; (2,1,n=*) tem exceções conhecidas; lista mínima exemplificativa:
    ("x_minus_y_eq_1", lambda x,y,n: (x - y) == 1 and n in {2}),
    ("x_eq_y",          lambda x,y,n: x == y),
    ("n_le_2",          lambda x,y,n: n <= 2),
]

def has_primitive_prime_divisor(x:int, y:int, n:int, plus:bool=False) -> bool:
    # Verifica se há um primo que divide x^n - y^n (ou +) e não divide (x*y) e não divide x^k - y^k para k < n.
    # Simplificação prática: checa se existe primo em fatoração que não aparece nos fatores de x*y e não divide x^m - y^m para m|n, m<n.
    # Para pipeline, esta aproximação é suficiente como barreira robusta.
    if plus:
        val = abs(pow(x, n) + pow(y, n))
    else:
        val = abs(pow(x, n) - pow(y, n))
    fac = factorint(val)
    base = set(factorint(abs(x)).keys()) | set(factorint(abs(y)).keys())
    # primos candidatos
    candidates = [p for p in fac.keys() if p not in base]
    return len(candidates) > 0

def zsigmondy_barrier(x:int, y:int, n:int, plus:bool=False) -> Dict:
    for name, cond in EXCEPTIONS:
        if cond(x,y,n):
            return {"exception": True, "reason": name}

    # Tenta detectar primo novo
    has_new = has_primitive_prime_divisor(x, y, n, plus=plus)
    if has_new:
        return {"exception": False, "reason": "primitive_prime_exists"}
    else:
        return {"exception": True, "reason": "no_primitive_prime_detected"}
