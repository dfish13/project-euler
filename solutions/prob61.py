
N = 6
polyList = []

for i in range(1, N+1):
	j = 1
	p = 1
	l = []
	while p < 1000:
		p += i*j + 1
		j += 1
	while p < 10000:
		l.append(p)
		p += i*j + 1
		j += 1
	polyList.append(l)

polyDict = []
for l in polyList:
	d = dict()
	for n in l:
		s = str(n)[:2]
		d[s] = d.get(s, []) + [n]
	polyDict.append(d)

def getNums(nnList, pDict, s):
	l = []
	for i in range(len(pDict)):
		if i not in nnList:
			l += [(i, x) for x in pDict[i].get(s, [])]
	return l

def helper(cur, nums):
	for n in nums:
		cur.append(n)
		if len(cur) == N and str(cur[0][1])[:2] == str(cur[N-1][1])[2:]: 
			print(cur)
			print(sum(x[1] for x in cur))
		nnums = getNums([x[0] for x in cur], polyDict, str(n[1])[2:])
		if len(nnums) > 0:
			helper(cur, nnums)
		cur.pop()

helper([], [(N-1, x) for x in polyList[N-1]])			
