
l = [1, 2, 2, 2, 2, 2]

e = [2]

fracs = []

for i in range(2, 70, 2):
	e += [1, i, 1]

for j in range(1, len(e)):
	i = len(e) - j
	num, den = (0, 1)
	while i >= 0:
		num = e[i]*den + num
		num, den = den, num
		i -= 1
	fracs.insert(0, (den, num))
fracs.insert(0, (2, 1))

print(sum(int(x) for x in str(fracs[99][0])))