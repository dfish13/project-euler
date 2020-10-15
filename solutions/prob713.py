import itertools
import numpy

N = 8
m = 4

C =  list(itertools.combinations(list(range(N)), m)) 

P =  list(itertools.combinations(list(range(N)), 2))

minVal = 1000
while 1:
	CC = C.copy()
	i = 0
	while len(CC) > 0:
		CC = [c for c in CC if not (P[i][0] in c and P[i][1] in c)]
		i += 1
	if i < minVal:
		minVal = i
		print('{} : {}'.format(i, P[:i]))
	numpy.random.shuffle(P) 

