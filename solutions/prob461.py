import math

class BST:

    def __init__(self, v):
        self.root

lim = 200

n = 0
while math.exp(n/lim) - 1 < math.pi:
    n += 1


nums = [(i, math.exp(i/lim) - 1) for i in range(n)]

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        s = nums[i][1] + nums[j][1] 
        if s < math.pi:
            pairs.append((i, j, s))

print(pairs[:20])
