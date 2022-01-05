# Number theoretical functions

import unittest


def int_square_root(n):
	"""
	Returns the integer square root of n, i.e. the number g
	s.t.  g^2 <= n < (g+1)^2
	"""
	if n < 0:
		raise ValueError()
	g = n // 2
	j = g // 2 or 1 
	while 1:
		if g**2 <= n:
			if n < (g+1)**2:
				return g
			else:
				g += j
		else:
 			g -= j
		j = j // 2 or 1 

def is_perfect_square(n):
	return int_square_root(n)**2 == n

def sqrt_continued_fraction(n):
	"""
	list where first value is the integer part and the rest is the repeating portion
	for example sqrt_continued_fraction(14) -> [3, 1, 2, 1, 6]
	"""
	ip = int_square_root(n)
	conFrac = [ip]
	if ip ** 2 == n:
		return conFrac
	num = 1
	den = ip
	while 1:
		top = den + ip
		bot = (n - den * den) // num
		y = top // bot
		conFrac.append(y)
		num = bot
		den = - (den - bot * y)
		if num == 1 and den == ip:
			return conFrac

def combinations(l, n):
	if n == 0:
		yield []
	prev = None
	i = 0
	while i < len(l):
		prev = l[i]
		for c in combinations(l[:i] + l[i + 1:], n - 1):
			yield [l[i]] + c
		i += 1





class TestMethods(unittest.TestCase):
	
	def test_int_square_root(self):
		self.assertEqual(int_square_root(3), 1)
		self.assertEqual(int_square_root(0), 0)
		self.assertEqual(int_square_root(1), 1)
		self.assertEqual(int_square_root(4), 2)
		self.assertEqual(int_square_root(5), 2)
		self.assertEqual(int_square_root(169), 13)
		self.assertEqual(int_square_root(170), 13)
		self.assertEqual(int_square_root(123456789), 11111)
		self.assertEqual(int_square_root(123454321), 11111)
		
		with self.assertRaises(ValueError):
			int_square_root(-3)

	def test_is_perfect_square(self):
		self.assertTrue(is_perfect_square(169))
		self.assertFalse(is_perfect_square(15))

	def test_combinations(self):
		C  = list(combinations([1, 1, 1, 2], 2))
		self.assertEqual(len(C), 18)

if __name__ == '__main__':
	unittest.main()
