"""
Find the smallest number n such that the number of divisors of n is equal to (2 ^ 500500)
"""

import heapq
from sympy import sieve

sieve.extend_to_no(500500)

H = [(3, 3, 1), (4, 2, 3)]
i = 3   # next prime to add from sieve (indexing starts at 1 so 3 would mean the 3rd prime (5))
n = 2   # number so far (mod 500500507)
for _ in range(2, 500501):
  p = heapq.heappop(H)
  if p[2] == 1:
    heapq.heappush(H, (sieve[i], sieve[i], 1))
    i += 1
  nextE = (p[2] + 1) * 2 - 1
  heapq.heappush(H, (p[1] ** (nextE - p[2]), p[1], nextE))
  n *= p[0]
  n %= 500500507

print(n)
