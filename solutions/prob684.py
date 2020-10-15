
modVal = 1000000007

fibList = [0, 1]

for i in range(89):
	fibList.append(fibList[-2] + fibList[-1])

def n2eMod(n, e, m):
	if not e > 0:
		return 1
	p = n
	v = 1
	for i in range(64):
		if (e >> i) & 1:
			v = (v * p) % m
		p = (p * p) % m
	return v		
 

def S(n):
	r = n % 9
	i = n // 9
	t = n2eMod(10, i, modVal)
	return 5*(t - 1) - 9*i + t*(r+2)*(r+1)//2 - (r + 1)

print(S(1))
print(S(20))	
print(sum(S(f) for f in fibList[2:]) % modVal)
