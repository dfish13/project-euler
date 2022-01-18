"""
A bunch of helpful graph functions that assume the input graph
is a list of n vertices [0, .., n-1]
and is given as an adjacency list.

Graph is unweighted and undirected

Example:
[
  [1, 2, 3],
  [2],
  [0, 1],
  [3]
]
"""

import numpy as np
from collections import defaultdict, deque
import matplotlib.pyplot as plt
from heapq import *
import unittest


def convert_to_canonical(edges, isolated_vertices=None):
  """
  Takes as input a list of edges of a Graph where the vertices are some immutable type i.e.
  strings or integers and returns and adjacency list for an equivalent graph in the form
  that is used in the library below. It also returns an array that maps the vertices in 
  [0 .. n - 1] back to their original immutable values.
  """

  n = 0
  def inc():
    nonlocal n
    n += 1
    return n - 1

  map = defaultdict(inc)
  adj = defaultdict(list)

  for e in edges:
    adj[map[e[0]]].append(map[e[1]])
  
  for v in isolated_vertices:
    dummy = map[v]
  
  d = [0] * n
  for k, i in map.items():
    d[i] = k
  return adj, d

class Graph:

  def __init__(self, adj, n=None):
    self.adj = adj
    self.n = n if n else len(self.adj)

  def from_edge_list(self, edges, n, undirected=False):
    self.adj = [[] for i in range(n)]
    for e in edges:
      self.adj[e[0]] = e[1]
      if undirected:
        self.adj[e[1]] = e[0]
    self.n = n

  def is_dag(self):
    pass

  def topological_sort(self):
    """
    Returns a list of topologically sorted vertices L. Graph must be a DAG (Directed
    Acyclic Graph) in order for a topological sorting of vertices to exist.

    Definition of topological sort:
    If the graph G contains an edge (u, v) then the vertex u appears before v in any
    topological sort of G.

    Note: multiple valid topological sorts of a Graph G may exist. 
    """

    visited = [0] * self.n
    rsort = []
    def dfs(u):
      if not visited[u]:
        visited[u] = 1
        for v in self.adj[u]:
          dfs(v)
        rsort.append(u)

    for i in range(self.n):
      dfs(i)
    
    return rsort[::-1]
        

  def shortest_path(self, u, v):
    """
    Returns a list of vertices which represent one of the shortest paths
    from the source vertex u to the target v.
    
    If the is no such path, return None.
    """
    if u == v:
      return [u]

    Q = deque()
    pred = [None] * len(self.adj)
    visited = [0] * len(self.adj)
    Q.append(u)
    visited[u] = 1

    def get_path(b):
      path = [b]
      while pred[b] is not None:
        path.append(pred[b])
        b = pred[b]
      return path[::-1]

    while len(Q):
      s = Q.popleft()
      for a in self.adj[s]:
        if visited[a] == 0:
          pred[a] = s
          if a == v:
            return get_path(a)
          Q.append(a)
          visited[a] = 1

    return None


class WGraph:
  """
  This class encapsulates a weighted graph and has some algorithms implemented to
  do various things on a weighted graph like find the shortest path for example using
  Djikstra's algorithm.

  Vertices are integers in the range [0 .. n - 1].
  """
  def __init__(self, adj=None):
    """
    Takes in an adjacency list of edges and their corresponding weights. Assumes the input
    is a directed graph i.e. if there is an edge (j, w) in adj[i] it does not mean there
    is necessarily (i, w) in adj[j]. For an undirected graph using an adjacency list
    representation this would be necessarily true.
    """
    self.adj = adj
    self.n =  None if self.adj is None else len(self.adj)
    self.source = -1
    self.target = -1

  def from_edge_list(self, edges, n, undirected=False):
    self.adj = [[] for i in range(n)]
    self.n = n
    for u, v, w in edges:
      self.adj[u].append((v, w))
      if undirected:
        self.adj[v].append((u, w))
  
  def shortest_path(self, u, v):
    """
    Returns a list representing one of the (possibly multiple) shortest paths from vertex u
    to vertex v or None if there is no path.   
    """
    self.djikstra(u, v)
    n = v
    path = []
    while n is not None:
      path.append(n)
      n = self.pred[n]
    if len(path) > 1:
      return path[::-1]
    return None

  def len_shortest_path(self, u, v):
    self.djikstra(u, v)
    return self.dist[v][0]

  def num_shortest_path(self, u, v):
    self.djikstra(u, v)
    return self.dist[v][1]

  def djikstra(self, u, v):
    if (self.source, self.target) == (u, v):
      """
      Check if algo has been performed on source and target to avoid extra work. For
      example if calls to shortest_path, num_shortest_path, and len_shortest_path are
      made on the same source and target vertices they can all use the results of a single
      execution of Djikstra's algorithm to compute their results.
      """
      return
    self.source = u
    self.target = v
    self.pred = [None] * self.n
    self.dist = [[float('inf'), 0] for i in range(self.n)]
    self.dist[self.source] = [0, 1]

    heap = [(0, self.source)]
    while heap:
      d, n = heappop(heap)
      if d > self.dist[self.target][0]:
        break
      if d > self.dist[n][0]:
        continue
      for v, w in self.adj[n]:
        pathLen = d + w
        if pathLen > self.dist[v][0]:
          continue
        elif pathLen < self.dist[v][0]:
          self.pred[v] = n
          self.dist[v][0] = pathLen
          self.dist[v][1] = self.dist[n][1]
          heappush(heap, (pathLen, v))
        else:
          self.dist[v][1] += self.dist[n][1]
       

def gen_random_graph(n, e):
  return np.random.randint(n, size=(n, e))

def main():

  clothes = [
    ['undershorts', 'pants'],
    ['undershorts', 'shoes'],
    ['pants', 'shoes'],
    ['pants', 'belt'],
    ['shirt', 'belt'],
    ['shirt', 'tie'],
    ['belt', 'jacket'],
    ['tie', 'jacket'],
    ['socks', 'shoes'],
  ]
  
  (adj, d) = convert_to_canonical(clothes, isolated_vertices=['watch'])
  g = Graph(adj, len(d))
  top_sort = g.topological_sort()
  print([d[x] for x in top_sort])

  wg = WGraph()
  wg.from_edge_list()

class TestWGraphMethods(unittest.TestCase):

  def test_shortest_path(self):
    edges = [
      (0, 4, 2),
      (4, 6, 2),
      (6, 1, 2),
      (1, 3, 2),
      (3, 9, 1),
      (4, 5, 2),
      (4, 7, 5),
      (7, 2, 5),
      (5, 2, 3),
      (2, 6, 2),
      (6, 8, 5),
      (4, 1, 4)
    ]
    wg = WGraph()
    wg.from_edge_list(edges, 10, undirected=True)

    self.assertEqual(wg.len_shortest_path(0, 9), 9)
    self.assertEqual(wg.num_shortest_path(0, 9), 2)
    self.assertEqual(wg.shortest_path(0, 2), [0, 4, 6, 2])

if __name__ == '__main__':
  unittest.main()