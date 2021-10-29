from sympy.ntheory import totient, factorint

def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

minRatio = 10**8
minN = 1
for n in range(3, 10**7 + 1, 2):
    totientN = totient(n)
    if is_perm(n, totientN) and (n / totientN) < minRatio:
        minN = n
        minRatio = n / totientN
    
print(minN, totient(minN), factorint(minN).items())
