from sympy import totient

maxn = 6
maxq = 3

for i in range(2, 1000000):
	q = i / totient(i)
	if q > maxq:
		maxq = q
		maxn = i
print("{} / {} = {}".format(maxn, totient(maxn), maxq))
