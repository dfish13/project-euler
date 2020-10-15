
N = 6
polyLists = []

for i in range(1, N+1):
	j, p, l = (1, 1, [])
	while p < 1000:
		p += i*j + 1
		j += 1
	while p < 10000:
		l.append(p)
		p += i*j + 1
		j += 1
	polyLists.append(l)

def f(a, index, nums):
	for i in range(N-1):
		if i not in index:
			for j in polyLists[i]:
				if a % 100 == j // 100:
					nums.append(j)
					index.append(i)
					if len(nums) == 6 and nums[0] // 100 == nums[N-1] % 100:
						print(nums)
						print(sum(nums))
					f(j, index, nums)
					nums.pop()
					index.pop()

for i in polyLists[N-1]:
	f(i, [N-1], [i])		
