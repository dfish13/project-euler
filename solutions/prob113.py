from math import comb

def partitions_with_zero(s, l):
    if s == 0:
        return 1
    count = 0
    for i in range(s):
        if i + 1 <= l:
            count += comb(s - 1, i) * comb(l, l - (i + 1))
    return count

count = 0
for d in range(1, 101):
    for i in range(1, 10):
        for s in range(9 - i, 0, -1):
            count += partitions_with_zero(s, d - 1)
    for i in range(1, 10):
        for s in range(i, -1, -1):
            count += partitions_with_zero(s, d - 1)

print(count)
        
