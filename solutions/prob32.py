from sympy.ntheory.factor_ import divisors

def is_pandigital_product(a, b, c):
    s = str(a) + str(b) + str(c)
    l = list(s)
    l.sort()
    return ''.join(l) == '123456789'

panNums = set()
for n in range(1234, 9876):
    divs = divisors(n)
    for d in divs[:len(divs)//2]:
        if is_pandigital_product(d, n//d, n):
            print('{} * {} = {}'.format(d, n//d, n))
            panNums.add(n)

print(sum(panNums))
