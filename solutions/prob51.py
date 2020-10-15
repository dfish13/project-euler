from sympy import isprime

def masks(d):
    for i in range(1, 2**d):
        yield [(i >> shift) & 1 for shift in range(d-1, -1, -1)]

d = 5
while True:
    for m in masks(d):
        for i in range(10**(d - sum(m))):
            notPrimeCount = 0
            for r in range(10):
                s = []
                si = str(i)
                si = '0'*(d - sum(m) - len(si)) + si
                sindex = 0
                for b in m:
                    if b:
                        s.append(str(r))
                    else:
                        s.append(si[sindex])
                        sindex += 1
                num = int(''.join(s))
                if len(str(num)) != d or not isprime(num):
                    notPrimeCount += 1
                if notPrimeCount > 2:
                    break   
            if notPrimeCount <= 2:
                print(m, num)
                exit(0)
    d += 1

          
