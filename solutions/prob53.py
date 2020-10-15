from sympy import binomial

total = 0
for n in range(101):
    if n % 2 == 0:
        if binomial(n, n//2) > 1000000:
            print('({}, {})'.format(n, n//2))
            total += 1
    for i in range((n // 2) + 1, n):
        if binomial(n, i) > 1000000:
            print('({}, {})'.format(n, i))
            print('({}, {})'.format(n, n-i))
            total += 2
        else:
            break

print(total)