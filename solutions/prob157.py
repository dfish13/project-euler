from sympy import divisors, divisor_count

def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    while y != 0:
        (x, y) = (y, x % y)
    return x

def num_solutions(n):
    total = 0
    divs = divisors(100**n)
    for d in divs[:(len(divs) // 2) + 1]:
        a = d + 10**n
        b = (100**n) // d + 10**n
        total += divisor_count(gcd(a, b))
    return total

print(sum(num_solutions(x) for x in range(1, 10)))
