

def is_pandigital(s):
    ls = list(s)
    ls.sort()
    return ''.join(ls) == '123456789'

for n in range(9000, 10000):
    if is_pandigital(str(n) + str(2*n)):
        print('{} -> {}'.format(n, str(n) + str(2*n)))
