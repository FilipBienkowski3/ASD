#Filip Bieńkowski
#Algorytm polega na znalezieniu ścieżki z a do b z najmniejszą możliwą wagą, do wykonania tego zadania zastosowałem algorytm zaimplementowany na zajęciach (dijkstra), który zmodyfikowany tak aby zwracał sume wag gdy znajdzie poszukiwany wierzchołek b spełnia założenia zadania.
#Z podanych tablic E oraz S stowrzyłem tablice G (graf) z dodatkowym wierzchołkiem, który jest tzw. pośrednikiem między wierzchołkami z tablicy S, który łaczy je wagą 0. Dorobienie wierzchołka pozwoliło mi na zmienjszenie złożoności obliczeniwej.
#Złożoność O(E+S+ElogE)
from zad5testy import runtests
from queue import PriorityQueue
inf = float('inf')

def spacetravel( n, E, S, a, b ):
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
  G=[[] for _ in range(n+1) ]
  for i in range(len(E)):
    x,y,z= E[i]
    G[x].append((y,z))
    G[y].append((x,z))
  for el in S:
    G[n].append((el,0))
    G[el].append((n,0))

  return dijkstra(G,a,b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )