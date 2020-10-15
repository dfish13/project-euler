from sympy import isprime

dprimes = 0
d = 1
i = 1
while True:
    dprimes += sum(isprime((2*i+1)**2 - j*i) for j in range(2, 7, 2))
    d += 4
    print(dprimes/d)
    if dprimes / d < 0.1:
        print(2*i+1)
        break
    i += 1
