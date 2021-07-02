

def isBouncy(n):
    l = [int(c) for c in str(n)]
    s = sorted(l)
    if l == s or l == s[::-1]:
        return False
    return True

n = 1
numBouncy = 0
proportion = 0.99
while 1:
    if isBouncy(n):
        numBouncy += 1
    if numBouncy / n >= proportion:
        break
    n += 1

print(n)