# Cubic Permutations

(0, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 2)


def num2tup(n):
    h = dict()
    for d in str(n):
        h[int(d)] = h.get(int(d), 0) + 1
    t = []
    for i in sorted(h.items(), key=lambda x: x[0]):
        t += i
    return tuple(t)


h = dict()

n = 1
while True:
    n2p = num2tup(n**3)
    l = h.get(n2p, [])
    l += [n**3]
    if len(l) == 5:
        print(l)
        break
    h[n2p] = l
    n += 1
