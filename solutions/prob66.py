import sys

sys.path.append('/home/duncanfish/git/project-euler')

from lib.ntheory import sqrt_continued_fraction, is_perfect_square

maxX = 0
maxD = 0
for d in range(2, 1001):
    if not is_perfect_square(d):
        conFrac = sqrt_continued_fraction(d)
        if len(conFrac) % 2:
            conFrac.pop()
        else:
            conFrac = conFrac + conFrac[1:-1]
        i = len(conFrac) - 1
        num, den = (0, 1)
        while i >= 0:
            num = conFrac[i] * den + num
            num, den = den, num
            i -= 1
        x, y = (den, num)
        if x > maxX:
            maxX = x
            maxD = d
        # print('{}^2 - {} * ({})^2 = 1'.format(x, d, y))

print(maxD)

