
def digit_sum(n):
    return sum(int(c) for c in str(n))

m = 0
for i in range(100):
    for j in range(100):
        s = digit_sum(i**j)
        m = s if s > m else m

print(m)