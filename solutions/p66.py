from lib.ntheory import is_perfect_square
from sympy.ntheory import primefactors



def xgen(p):
	n = 1
	while 1:
		yield n*p - 1
		yield n*p + 1
		n += 1
	
d = 2
s = 2
while 1:
	if d == s**2:
		d += 1
		s += 1
	p = primefactors(d)[-1]
	

	for x in xgen(p):
		n = x**2 - 1
		if n % d == 0:
			if is_perfect_square(n//d): 
				print('D = {}, x = {}'.format(d, x))
				break
	d += 1
	 	
