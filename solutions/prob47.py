from sympy.ntheory import primefactors


pf = primefactors
n = 645
while 1:
    n3 = pf(n+3)
    if len(n3) != 4:
        n += 4
        continue
    n2 = pf(n+2)
    if len(n2) != 4:
        n += 3
        continue
    n1 = pf(n+1)
    if len(n1) != 4:
        n += 2
        continue
    n0 = pf(n)
    if len(n0) != 4:
        n += 1
        continue
    break
print(n0, n1, n2, n3)
print(n)
