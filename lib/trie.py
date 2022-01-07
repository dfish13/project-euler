
from functools import lru_cache

class TrieNode:

  def __init__(self, weight = 0):
    self.children = [None] * 26
    self.weight = weight


class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, s, w):
    node = self.root

    for c in s:
      if node.children[ord(c) - ord('a')] is None:
        node.children[ord(c) - ord('a')] = TrieNode()
      node = node.children[ord(c) - ord('a')]
    node.weight = w
  
  def dfs(self, root):
    if root.weight > self.maxWeight:
      self.maxWeight = root.weight
    for i in range(26):
      if root.children[i]:
        self.dfs(root.children[i])

  @lru_cache(None)
  def search(self, prefix):
    node = self.root

    for c in prefix:
      if node.children[ord(c) - ord('a')] is None:
        return -1
      node = node.children[ord(c) - ord('a')]
    self.maxWeight = 0
    self.dfs(node)
    if self.maxWeight > 0:
      return self.maxWeight
    return -1

if __name__ == '__main__':
  T = Trie()

  import sys
  n, q = [int(x) for x in next(sys.stdin).split()]
  for i in range(n):
    s, w = next(sys.stdin).split()
    T.insert(s, int(w))
  
  for i in range(q):
    s = next(sys.stdin).strip()
    print(T.search(s))
      
