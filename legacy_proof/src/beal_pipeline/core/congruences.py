from typing import Dict, Tuple

def _is_perfect_power_mod(n: int, p: int) -> bool:
    # Para p pequeno, qualquer k^e mod p pode assumir valores no conjunto de resíduos de potências.
    # Aqui simplificamos: checamos se n mod p é congruente a algum x^2 ou x^3 para padrões simples.
    # Em produção, expandir para potências gerais conforme a, b, c.
    r = n % p
    # Quadrados mod p
    squares = { (x*x) % p for x in range(p) }
    # Cubos mod p (útil para padrões em potências ímpares)
    cubes = { (x*x*x) % p for x in range(p) }
    return (r in squares) or (r in cubes)

def quick_congruence_filters(x:int,y:int,z:int,a:int,b:int,c:int, mods=(2,3,4,5,8,9,11)) -> Dict:
    # Mod 2 (paridade)
    lhs2 = (pow(x, a, 2) + pow(y, b, 2)) % 2
    rhs2 = pow(z, c, 2)
    if lhs2 != rhs2:
        return {"discard": True, "reason": "parity_mismatch_mod2"}

    # Mod 4: padrões de quadrados e somas
    lhs4 = (pow(x, a, 4) + pow(y, b, 4)) % 4
    rhs4 = pow(z, c, 4)
    # Quadrados mod 4 são 0 ou 1; verificar incoerências comuns
    # Ex.: soma de dois números ≡ 2 mod 4 não pode ser potência par de inteiro ímpar, etc.
    if (lhs4 == 2 and rhs4 in {0,1}) or (lhs4 == 3 and rhs4 in {0,1}):
        return {"discard": True, "reason": "incompatible_mod4_pattern"}

    # Mod 3: quadrados ≡ 0 ou 1; cubos ≡ 0, ±1
    lhs3 = (pow(x, a, 3) + pow(y, b, 3)) % 3
    rhs3 = pow(z, c, 3)
    if lhs3 != rhs3:
        return {"discard": True, "reason": "mismatch_mod3"}

    # Mod 5: padrões de últimas cifras e potências (refina casos)
    lhs5 = (pow(x, a, 5) + pow(y, b, 5)) % 5
    rhs5 = pow(z, c, 5)
    if lhs5 != rhs5:
        return {"discard": True, "reason": "mismatch_mod5"}

    # Mod 8: quadrados de ímpares ≡ 1 mod 8; pares elevados geram 0 mod 8 rapidamente
    lhs8 = (pow(x, a, 8) + pow(y, b, 8)) % 8
    rhs8 = pow(z, c, 8)
    if lhs8 != rhs8:
        return {"discard": True, "reason": "mismatch_mod8"}

    # Mod 9: útil para padrões de cubos e somas de potências
    lhs9 = (pow(x, a, 9) + pow(y, b, 9)) % 9
    rhs9 = pow(z, c, 9)
    if lhs9 != rhs9:
        return {"discard": True, "reason": "mismatch_mod9"}

    # Mod 11: detection rápida de impossibilidades (refinamento adicional)
    lhs11 = (pow(x, a, 11) + pow(y, b, 11)) % 11
    rhs11 = pow(z, c, 11)
    if lhs11 != rhs11:
        return {"discard": True, "reason": "mismatch_mod11"}

    # Padrões simplificados de "ser potência" modulo p
    for p in (3,4,5,8,9,11):
        # Verificações heurísticas: z^c mod p deve ser compatível com resíduos de potências
        if not _is_perfect_power_mod(pow(z, c, p), p):
            return {"discard": True, "reason": f"z^c_not_power_like_mod{p}"}

    return {"discard": False}
