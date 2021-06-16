from math import log


L = []
with open('../static/p099_base_exp.txt', 'r') as dataFile:
    for i, l in enumerate(dataFile):
        b, e = (int(x) for x in l.split(','))
        L.append((i + 1, e, b))
print(max(L, key=lambda x : x[1] * log(x[2])))
