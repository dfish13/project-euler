

p = [(n*(3*n-1))//2 for n in range(1, 10000)]
pSet = set(p)

for i in range(len(p)):
    for j in range(i+1, len(p)):
        if p[j] - p[i] in pSet and p[j] + p[i] in pSet:
            print('{} - {} = {}'.format(p[j], p[i], p[j] - p[i]))
