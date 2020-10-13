from sympy.ntheory.factor_ import is_abundant

abundantNums = set(n for n in range(1, 28713) if is_abundant(n))

total = 0

for n in range(1, 28713):
    isSum = False
    for a in abundantNums:
        if a >= n:
            break
        elif (n-a) in abundantNums:
            isSum = True
            break

    if not isSum:
        total += n

print(total)
