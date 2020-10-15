import re
import math

pat = '1.2.3.4.5.6.7.8.9.0'

i = math.floor(1020304050607080900**0.5)
while i % 10 > 0:
	i += 1

while 1:
	z = re.match(pat, str(i**2))
	if z:
		print('{}^2 = {}'.format(i, i**2))
		break
	i += 10
