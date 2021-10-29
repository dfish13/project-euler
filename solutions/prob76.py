import numpy as np

P = np.zeros((101, 101), dtype=object)

for i in range(101):
    P[i][0] = 1

def Pfunc(n, k):
    return P[n - 1][k - 1]

for i in range(2, 102):
    for j in range(1, i + 1):
        total = 0
        if i == j:
            total += 1
            for k in range(1, i):
                if (i, j) == (5, 5):
                    print(Pfunc(i - k, k))
                total += Pfunc(i - k, k)
        else:
            for k in range(1, j + 1):
                total += Pfunc(i - k, k)
        P[i - 1][j - 1] = total

print(Pfunc(101, 101) - 1)
