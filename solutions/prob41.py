from sympy import isprime

from itertools import permutations

for p in permutations([str(x) for x in range(7, 0, -1)]):
    if isprime(int(''.join(p))):
        print(''.join(p))
        exit(0)
