# Number theoretical functions

import unittest


def int_square_root(n):
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

if __name__ == '__main__':
	unittest.main()
