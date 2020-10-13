

t = [(n*(n+1))//2 for n in range(285, 100000)]
pSet = set([(n*(3*n-1))//2 for n in range(1, 100000)])
hSet = set([n*(2*n-1) for n in range(1, 100000)])

for n in t:
    if n in pSet and n in hSet:
        print(n)
