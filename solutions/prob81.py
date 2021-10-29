import numpy as np

with open('../static/p081_matrix.txt', 'r') as mFile:
    L = []
    for l in mFile:
        L += list(int(x) for x in l.split(','))

    M = np.asarray(L)
    M = M.reshape((80, 80))

    A = np.zeros((80, 80))
    A[0][0] = M[0][0]
    print(A)

    for k in range(1, 159):
        i = 0
        while i <= k and i < 80:
            if (k - i) < 80:
                j = k - i
                vals = []
                if i - 1 >= 0:
                    vals.append(A[i - 1][j])
                if j - 1 >= 0:
                    vals.append(A[i][j - 1])
                print(min(vals))
                A[i][j] = min(vals) + M[i][j]
            i += 1
    
    print(A[79][79])
