

"""
Scratch Work:

R(1, 1) = 1
R(2, 1) = 3
R(2, 2) = 4 + 2 + 2 + 1 = 9


R(1, n) = R(1, n - 1) + n
R(1, n) = T(n) = (n + 1) * n / 2 

R(m, n) = R(m - 1, n) + T(n) * m

R(3, 2) = R(2, 2) + R(1, 2) * 3 = 9 + 3* 3 = 18

R(m, n) = sum_(i = 1)^(m) T(n) * i
 = T(m) * T(n)
 = 6 * 3
"""

def triangular(n):
    return ((n + 1) * n) // 2

def numRectangles(m, n):
    return triangular(m) * triangular(n)

triNums = []
a = 3
n = 3
while n <= 2000000:
    triNums.append((a - 1, n))
    n += a
    a += 1

c = (3, 3)
for x, i in triNums:
    for y, j in triNums:
        if abs(2000000 - i * j) < abs(2000000 - c[0] * c[1]):
            c = (i, j)
            ans = (x, y)

print('{} = {} * {}'.format(ans[0] * ans[1], ans[0], ans[1]))





