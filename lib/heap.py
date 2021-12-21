# Max Heap implementation

import unittest

class Heap:

  def __init__(self, L, comparator):
    pass

class MaxHeap:
  """
  Converts list to a heap in place.
  Beware, the class does not make a copy of the list!
  """

  def __len__(self):
    return len(self.L)

  def __init__(self, L, key=None):
    self.L = L
    self.heapify()
  
  def heapify(self):
    end = len(self.L) - 1
    start = (end - 1) // 2

    for i in range(start, -1, -1):
      self.percolate_down(i, end)

  def percolate_down(self, i, end):
    child = (2 * i) + 1
    while (2 * i) + 1 <= end:
      child = (2 * i) + 1
      if child + 1 <= end:
        child = child if self.L[child] > self.L[child + 1] else child + 1
      if self.L[child] > self.L[i]:
        self.L[child], self.L[i] = self.L[i], self.L[child]
        i = child
      else:
        return
  
  def percolate_up(self, i):
    while i > 0:
      parent = (i - 1) // 2
      if self.L[i] > self.L[parent]:
        self.L[i], self.L[parent] = self.L[parent], self.L[i]
      else:
        break
      i = parent
      
  def push(self, val):
    self.L.append(val)
    self.percolate_up(len(self.L) - 1)

  def pop(self):
    self.L[0] = self.L[-1]
    self.L.pop()
    self.percolate_down(0, len(self.L) - 1)

  def get_max(self):
    return self.L[0]

class TestMethods(unittest.TestCase):

  def test_heapify(self):
    L = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    H = MaxHeap(L)
    for i in range(len(L) // 2):
      if 2 * i + 1 < len(L):
        self.assertGreaterEqual(L[i], L[2 * i + 1])
      if 2 * i + 2 < len(L):
        self.assertGreaterEqual(L[i], L[2 * i + 2])

  def test_heap_get_max(self):
    L = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    H = MaxHeap(L)
    
    self.assertEqual(H.get_max(), 6)
    H.pop()
    self.assertEqual(H.get_max(), 5)

  def test_len(self):
    L = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    H = MaxHeap(L)
    self.assertEqual(len(L), len(H))

if __name__ == '__main__':
	unittest.main()