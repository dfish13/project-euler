import numpy as np

import unittest

class DisjSet:

  def __init__(self, n):
    self.A = np.full(n, -1)
  
  def find(self, x):
    if self.A[x] < 0:
      return x
    else:
      self.A[x] = self.find(self.A[x])
      return self.A[x]

  def union(self, x, y):
    r1 = self.find(x)
    r2 = self.find(y)
    if r1 == r2:
      return
    else:
      self.unionSets(r1, r2)

  def unionSets(self, r1, r2):
    """
    Assumes r1 and r2 are distinct roots
    Union by size
    """
    r1, r2 = (r1, r2) if self.A[r1] < self.A[r2] else (r2, r1)
    self.A[r1] += self.A[r2]
    self.A[r2] = r1
  
  def numSets(self):
    return sum((x < 0) for x in self.A)

  def connected(self, x, y):
    return self.find(x) == self.find(y)

class TestMethods(unittest.TestCase):

  def test_union_different_set(self):
    S = DisjSet(10)
    S.union(0, 5)
    S.union(0, 6)
    S.union(0, 7)
    S.union(2, 3)
    self.assertEqual(S.numSets(), 6)

  def test_union_same_set(self):
    S = DisjSet(10)
    S.union(0, 5)
    S.union(0, 6)
    S.union(0, 7)
    self.assertEqual(S.numSets(), 7)
    S.union(5, 7)
    self.assertEqual(S.numSets(), 7)
    

if __name__ == '__main__':
	unittest.main()