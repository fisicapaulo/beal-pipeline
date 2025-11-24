from typing import Dict
from sympy import factorint

def vp(n:int, p:int) -> int:
    if n == 0:
        return 10**9  # formal, não deve ocorrer no fluxo
    n = abs(n)
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def lte_val_minus(x:int, y:int, n:int, p:int) -> int:
    # LTE: v_p(x^n - y^n)
    # Se p | (x - y) e p ímpar: v_p(x^n - y^n) = v_p(x - y) + v_p(n)
    if p == 2:
        # Casos de 2 são mais delicados. Algumas variantes comuns:
        # Se x-y é par, e x,y ímpares: v2(x^n - y^n) = v2(x-y) + v2(n)
        # Se x,y pares, a normalização anterior deve ter reduzido gcd; tratamos genericamente:
        return vp(x - y, 2) + vp(n, 2)
    if (x - y) % p == 0:
        return vp(x - y, p) + vp(n, p)
    # Caso geral quando p ∤ (x - y): p pode dividir (x+y) se n é par (não aplicamos aqui)
    return 0

def lte_val_plus(x:int, y:int, n:int, p:int) -> int:
    # LTE: v_p(x^n + y^n)
    # Clássico: se p | (x + y) e n é ímpar: v_p(x^n + y^n) = v_p(x + y) + v_p(n)
    if p == 2:
        # Para 2, uma regra comum quando x,y são ímpares e n é ímpar:
        # v2(x^n + y^n) = v2(x + y)
        base = vp(x + y, 2)
        return base + (vp(n,2) if n % 2 == 1 else 0)
    if (x + y) % p == 0 and n % 2 == 1:
        return vp(x + y, p) + vp(n, p)
    return 0

def lte_check(x:int, y:int, a:int, b:int) -> Dict:
    # Avalia valuations previsíveis para p em fatores de x^a - y^a e x^a + y^a,
    # e compara coerência básica com a estrutura exigida por Beal.
    # Foco: consistência — se valuations sugerem impossibilidade ao casar lados.
    # Nota: o beal-pipeline usa estas leituras como barreiras, não como prova exaustiva.

    # Fatorações para inspeção
    fx = factorint(abs(x))
    fy = factorint(abs(y))

    primes = sorted(set(list(fx.keys()) + list(fy.keys())))
    notes = []
    contradictions = []

    # Checamos p em dois contextos: diferença e soma.
    for p in primes:
        vm_minus = lte_val_minus(x, y, a, p)
        vm_plus  = lte_val_plus(x, y, a, p)
        # Heurística: se vm_minus e vm_plus são ambos muito baixos, mas exigiria
        # alta valuation para compor igualdade com potências, marcar suspeita.
        if vm_minus == 0 and vm_plus == 0:
            notes.append(f"p={p}: no_LTE_gain")
        else:
            notes.append(f"p={p}: v_minus={vm_minus}, v_plus={vm_plus}")

    # Sinal: se x,y têm sinais diferentes e a é ímpar, x^a + y^a pode cancelar parcialmente.
    if (x < 0) ^ (y < 0) and (a % 2 == 1 or b % 2 == 1):
        notes.append("sign_mix_with_odd_exponent")

    return {
        "notes": notes,
        "contradiction": len(contradictions) > 0,
    }
