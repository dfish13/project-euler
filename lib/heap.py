# Max Heap implementation

import unittest

class MaxHeap:
  """
  Converts list to a heap in place.
  Beware, the class does not make a copy of the list!
  """
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

if __name__ == '__main__':
	unittest.main()