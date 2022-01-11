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

  N = 100

  adj = gen_random_graph(N, 3)
  g = Graph(adj)
  p = np.random.randint(N, size=2)

  print(adj)
  print(p)
  print(g.shortest_path(*p))

  x = np.arange(0, 5, 0.1)
  y = np.sin(x)
  plt.plot(x, y)
  plt.show()



if __name__ == '__main__':
  main()