import math


def are_coprime(a, b, c):
    return math.gcd(math.gcd(a, b), c) == 1


triples = set()

for n in range(1, 20):
    for m in range(n+1, 20):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        l = [a, b, c]
        l.sort()
        if are_coprime(a, b, c):
            triples.add(tuple(l))

for t in triples:
    print('{} -> {}'.format(t, sum(t)))





m = 0

for p in range(12, 1001):
    count = 0
    for t in triples:
        if p % sum(t) == 0:
            count += 1
    if count > m:
        m = count
        mv = p

print('There are {} solutions for p = {}'.format(m, mv))
