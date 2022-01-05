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
from collections import deque
import matplotlib.pyplot as plt


class Graph:

  def __init__(self, adj):
    self.adj = adj

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

  N = 100

  adj = gen_random_graph(N)
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