import math
p = 1
i = 1
while 0:
    ns = str(2 ** i)
    if len(ns) >= 3 and ns[:2] == '12':
        print('{} : 2 ** {} = {}'.format(p, i, ns if len(ns) <= 23 else ns[:20] + '...'))
        p += 1
    i += 1

i = 1
closest = 1
while 1:
    l = math.log10(2 ** i)
    minDif = min(math.ceil(l) - l, l - math.floor(l))
    if minDif < closest:
        closest = minDif
        print('{} -> 2 ** {}'.format(minDif, i))
    i += 1
