from sympy import primerange, isprime

def is_perm(a, b, c):
    while len(a) > 0:
        if a[0] in b:
            b.remove(a[0])
        if a[0] in c:
            c.remove(a[0])
        a.pop(0)
    return len(b) == 0 and len(c) == 0

for p in primerange(1000, 10000):
    i = 2
    while p + 2*i < 10000:
        if isprime(p+i) and isprime(p+2*i) and is_perm(list(str(p)), list(str(p+i)), list(str(p+2*i))):
            print('{}{}{}'.format(p, p+i, p+2*i))
        i += 2
