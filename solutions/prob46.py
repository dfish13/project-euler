from sympy import isprime

n = 33
while 1:
    s = 0
    isGoldbach = False
    while n > 2*(s**2):
        if isprime(n - 2*(s**2)):
            print('{} + 2*({}^2) = {}'.format(n - 2*(s**2), s, n))
            isGoldbach = True
            break
        s += 1
    if not isGoldbach:
        break
    n += 2
print(n)
