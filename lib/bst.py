"""
A Binary Search Tree class and a bunch of little functions doing some kind of binary
search.

Mostly just practice for learning the concepts of binary search.
"""

import unittest


def find_closest(A, n):
  """
  Finds the element x in A for which abs(x - n) is minimized.
  A should be non empty.
  """
  lo = 0
  hi = len(A) - 1
  ans = 0
  dif = abs(A[ans] - n)
  while lo <= hi:
    mid = (lo + hi) // 2
    if A[mid] < n:
      lo = mid + 1
    elif A[mid] > n:
      hi = mid - 1
    else:
      return A[mid]
    if abs(A[mid] - n) < dif:
      ans = mid
      dif = abs(A[ans] - n)
  return A[ans]


def approximate_sqrt(n, epsilon):
  """
  Calculates the square root of n to an error of less than epsilon 
  """
  lo = 0.0
  hi = float(n)
  while (hi - lo) > epsilon:
    mid = (lo + hi) / 2
    if mid ** 2 > n:
      hi = mid
    else:
      lo = mid
  return mid

def integer_sqrt(n):
  """
  Finds the largest number x s.t. x ** 2 is less than or equal to n.
  """
  lo = 0
  hi = n
  ans = lo + (hi - lo) // 2
  while lo <= hi:
    mid = lo + (hi - lo) // 2
    if mid * mid <= n:
      ans = mid
      lo = mid + 1
    else:
      hi = mid - 1
  return ans

def smallest_element_in_rotated_array(a):
  lo = 0
  hi = len(a) - 1
  ans = a[0]
  while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] < a[0]:
      ans = a[mid]
      hi = mid - 1
    else:
      lo = mid + 1
  return ans


def bisect_left(a, x, lo=0, hi=None, key=None):
  """
  Loop Invariant 1: lo always points to an element that is strictly less than x,
  or -1 if there are no elements less than x.
  
  Loop Invariant 2: hi always points to an element that is greater than or equal
  to x or len(a) if all elements are stricly less than x.

  Loop Invariant 3: while inside the loop , lo and hi differ by at least 2.

  Progress Criteria: because of loop invariant 3, mid always sits between lo and hi
  and isn't equal to either of them so we are always moving closer to the desired
  index.

  At the end hi points to the index where we would insert an element to keep the list
  in sorted order. Note that hi could potentially still equal len(a) which is an invalid
  index for the list.
  """
  if hi is None:
    hi = len(a) - 1
  ans = len(a)
  while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] >= x:
      ans = mid
      hi = mid - 1
    else:
      lo = mid + 1
  return ans

class TreeNode():

  def __init__(self, val=0, left=None, right=None, h=1):
    self.val = val
    self.left = left
    self.right = right
    self.h = h
  
class BST():
  """
  AVL Tree
  This is an implementation of a balanced binary tree. For any node, the height of
  its left and right subtrees differ by at most 1.
  """

  def __init__(self):
    self.root = None

  def find_closest(self, val):
    """
    Returns the value of the element in the tree with a value closest to val.
    If the tree is empty return None.
    If the value exists in the array, return that value.
    """
    return self._find_closest(self.root, val)
  
  def _find_closest(self, root, val):
    if root is None:
      return None
    if root.val == val:
      return val
    elif root.val > val:
      rootDif = root.val - val
      subTreeVal = self._find_closest(root.left, val)
    else:
      subTreeVal = self._find_closest(root.right, val)
      rootDif = val - root.val
    if subTreeVal is None:
      return root.val
    subTreeDif = abs(subTreeVal - val)
    return root.val if rootDif < subTreeDif else subTreeVal
    

  def find(self, val):
    return self._find(self.root, val)


  def _find(self, root, val):
    if root is None:
      return None
    if root.val < val:
      return self._find(root.right)
    elif root.val > val:
      return self._find(root.left)
    return root

  def _h(self, n):
    return (0 if n is None else n.h)
  
  def _bf(self, n):
    return self._h(n.right) - self._h(n.left)

  def _insert(self, root, val):
    if val < root.val:
      if root.left:
        self._insert(root.left, val)
      else:
        root.left = TreeNode(val)
        root.bf -= 1
    elif val > root.val:
      if root.right:
        self._insert(root.right, val)
      else:
        root.right = TreeNode(val)
    else:
      # val already exists in the tree so just return.
      # if this was a multiset we could keep a counter of the number of occurences of the value
      return


  def insert(self, val):
    if self.root is None:
      self.root = TreeNode(val)
    else:
      self._insert(self.root, val)


class TestMethods(unittest.TestCase):

  def test_bisect_left(self):
    import bisect
    L = list(range(50))
    test_vals = [3, 30, 60, -2, 9, 25]
    for v in test_vals:
      i = bisect_left(L, v)
      self.assertEqual(i, bisect.bisect_left(L, v))

  def test_bst(self):
    pass
  
  def test_approximate_sqrt(self):
    epsilon = 1e-13
    for n in range(2, 11):
      s = approximate_sqrt(n, epsilon)
      self.assertLess(abs(n - s * s), 2 * s * epsilon + epsilon ** 2)
  
  def test_int_square_root(self):
    self.assertEqual(integer_sqrt(3), 1)
    self.assertEqual(integer_sqrt(0), 0)
    self.assertEqual(integer_sqrt(1), 1)
    self.assertEqual(integer_sqrt(4), 2)
    self.assertEqual(integer_sqrt(5), 2)
    self.assertEqual(integer_sqrt(169), 13)
    self.assertEqual(integer_sqrt(170), 13)
    self.assertEqual(integer_sqrt(123456789), 11111)
    self.assertEqual(integer_sqrt(123454321), 11111)
  
  def test_find_closest(self):
    A = [-39, -2, 3, 3, 4, 6, 9, 25, 30, 42, 42, 42, 60, 88]
    self.assertEqual(find_closest(A, 7), 6)
    self.assertEqual(find_closest(A, 25), 25)
    self.assertEqual(find_closest(A, 100), 88)
    self.assertIn(find_closest(A, 5), [4, 6])


if __name__ == '__main__':
  unittest.main()
      
