
def addSquareDigs(n):
	return sum(int(d)**2 for d in str(n))  

count = 0

S1 = set()
S1.add(1)

S89 = set()
S89.add(89)


for i in range(1, 10000000):
	l = []
	n = i
	while 1:
		if n in S1:
			for num in l:
				S1.add(num)
			break
		elif n in S89:
			for num in l:
				S89.add(num)
			count += 1
			break
		n = addSquareDigs(n)
		l.append(n)


print(S89)
print(S1)

print(count)
print(len(S89))
	
