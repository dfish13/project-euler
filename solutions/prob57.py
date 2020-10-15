from math import gcd

def reduce(a, b):
    g = gcd(a, b)
    return (a // g, b // g)

a, b = 1, 2

count = 0
for i in range(1000):
    c , d = reduce(a + b, b)
    if len(str(c)) > len(str(d)):
        count += 1
    a, b =  reduce(b, 2 * b + a)

print(count)    

