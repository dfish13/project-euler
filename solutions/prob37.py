from sympy import isprime


def is_truncatable(n):
    if not isprime(n):
        return False
    sn = str(n)
    for i in range(len(sn) - 1):
        if not (isprime(int(sn[i+1:])) and isprime(int(sn[:-(i+1)]))):
            return False
    return True

total = 0
for n in range(23, 1000000):
    if is_truncatable(n):
        print(n)
        total += n

print(total)
