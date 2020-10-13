from sympy import isprime


numCircularPrimes = 0
for n in range(2, 1000000):
    isCircularPrime = True
    if not isprime(n):
        continue
    ln = list(str(n))
    for i in range(len(ln)-1):
        d = ln.pop()
        ln.insert(0, d)
        if not isprime(int(''.join(ln))):
            isCircularPrime = False
            break
    if isCircularPrime:
        print(n)
        numCircularPrimes += 1

print(numCircularPrimes)
