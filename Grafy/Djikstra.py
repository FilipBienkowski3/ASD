#wagi nieujemne
#nieskierowany
#macierzowa (v^2)
#listowa (eloge)
from queue import PriorityQueue

inf = float('inf')



def dijkstraM(M, s):
    n = len(M)
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0

    for _ in range(n):
        u = -1
        distance = inf
        for i in range(n):
            if not visited[i] and distance > d[i]:
                u = i
        d[u] = distance
        visited[u] = True
        for v in range(n):
            if M[u][v] >= 0 and d[v] > d[u] + M[u][v]:
                parent[v] = u
                d[v] = d[u] + M[u][v]
    return d, parent


# O(V^2)
#listowa

def dijkstra(M, s):
    n = len(M)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s, -1))
    while not q.empty():
        distance, u, p = q.get()
        # if u==t:
        #   return distance
        if d[u] == inf:
            d[u] = distance
            parent[u] = p
            for (v, w) in M[u]:
                if d[v] == inf:
                    q.put((d[u] + w, v, u))
    return d, parent 


# O(E log E)



def dijkstrarelaksaxja(M, s):
    n = len(M)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()

    q.put((0, s, -1))

    while not q.empty():
        distance, u, p = q.get()
        if d[u] == inf:
            d[u] = distance
            parent[u] = p
            for (v, w) in M[u]:
                if d[v]>d[u]+w:
                  #d[v]=d[u]+w
                  q.put((d[u] + w, v, u))
    return d, parent 
def path(M, s, t):
    d, parent = dijkstra(M, s,t)
    path = []
    u = t
    while u != s:
        path.append(u)
        u = parent[u]
    path.append(s)
    path = path[::-1]
    return path


def dijkstra(G, s,t):
  n = len(G)
  d = [inf for _ in range(n)]
  parent = [None for _ in range(n)]
  q = PriorityQueue()
  q.put((0, s, -1))
  while not q.empty():
    distance, u, p = q.get()
    if u==t:
      return distance
    if d[u] == inf:
      d[u] = distance
      parent[u] = p
      for (v, w) in G[u]:
        if d[v] == inf:
          q.put((d[u] + w, v, u))



G = [[(1, 1), (4, 3)], [(0, 1), (2, 1)], [(3, 4), (1, 1)],
     [(2, 4), (5, 1), (6, 100)], [(0, 3), (5, 4)], [(4, 4), (3, 1)],
     [(3, 100)]]
G2=[[(1,1),(7,1)],[(0,1),(4,3),(2,3)],[(1,3),(3,5)],[(2,4),(4,2),(6,1)],[(1,3),(7,1),(5,3),(3,2)],[(4,3),(8,1),(6,8)],[(5,8),(3,1),(8,4)],[(0,2),(4,1),(8,7)],[(7,7),(5,1),(6,4)]]
G3=[[(1,2),(2,4),(3,2)],[],[],[(2,8),(4,3)],[]]
print(dijkstra(G3, 0))
print(dijkstrarelaksaxja(G3,0))
print(dijkstra(G3, 0, 4))












def dijkstra(G, s,t):
  n = len(G)
  d = [inf for _ in range(n)]
  parent = [None for _ in range(n)]
  q = PriorityQueue()
  q.put((0, s, -1))
  while not q.empty():
    distance, u, p = q.get()
    if u==t:
      return distance
    if d[u] == inf:
      d[u] = distance
      parent[u] = p
      for (v, w) in G[u]:
        if d[v] == inf:
          q.put((d[u] + w, v, u))