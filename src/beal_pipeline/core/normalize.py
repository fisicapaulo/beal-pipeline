import math

def normalize_row(row):
    x,y,z,a,b,c = int(row.x), int(row.y), int(row.z), int(row.a), int(row.b), int(row.c)
    if min(a,b,c) <= 2:
        return {"status":"discard","reason":"exponent<=2"}
    g = math.gcd(math.gcd(abs(x),abs(y)),abs(z))
    x2,y2,z2 = x//g, y//g, z//g
    return {"status":"ok","x":x2,"y":y2,"z":z2,"a":a,"b":b,"c":c,"g":g}
