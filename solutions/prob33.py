

def fake_reduce(a, b):
    la = list(str(a))
    lb = list(str(b))
    if '0' in la or '0' in lb:
        return (a, b)
    if la[0] in lb:
        lb.remove(la[0])
        la.pop(0)
        if la[0] in lb:
            return (a, b)
    elif la[1] in lb:
        lb.remove(la[1])
        la.pop(1)
    return (int(''.join(la)), int(''.join(lb)))


for a in range(10, 100):
    for b in range(a, 100):
        (c, d) = fake_reduce(a, b)
        if (a * d) == (b * c) and (a, b) != (c, d):
            print('{}/{} = {}/{}'.format(a, b, c, d))
