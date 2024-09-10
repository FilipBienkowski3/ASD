#Filip Bieńkowski
#Algorytm polega na znalezieniu najkrótszej ścieżki z s do t, dzięki BFS, nastepnie wszystkie krawedzie tej ścieżki są wpisywane do tablicy edges.
#W pętli powstaje nowy graf H bez odpowiednio danej krawedzi z edges, wywołuję funkcje BFS dla grafu H, która zwraca nową odległość między wierzchołkami.
#Algorytm kończy działanie, gdy znajdzie krawędz powodującą wydłużenie pierwotnej ścieżki.
#Złożoność O((V+E)*E)
from zad4testy import runtests
from collections import deque
def bfs(G,t,s):
  n=len(G)
  number=[-1 for i in range(n)]
  number[s]=0
  Q=deque()
  Q.append(s)
  while Q and number[t]==-1:
    u=Q.popleft()
    for v in G[u]:
      if number[v]==-1:
        number[v]=number[u]+1
        Q.append(v)
  if number[t] == -1:
    return float('inf')
  return number[t]
def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    number = [-1 for i in range(n)]
    number[s] = 0
    Q = deque()
    Q.append(s)
    while Q and number[t]==-1:
        u = Q.popleft()
        for v in G[u]:
            if number[v]==-1:
                number[v] = number[u] + 1
                Q.append(v)
    if number[t]==-1:
        return None
    leng = number[t]
    edges=[]
    k = t
    for i in range(leng - 1, -1, -1):
        for v in G[k]:
            if number[v] == i:
                edges.append((v, k))
                k = v
                break
    krotka = None
    maxi = leng
    p=0
    while leng > 0:
        u=edges[p]
        H = G.copy()
        x = u[0]
        y = u[1]
        H[x].remove(y)
        H[y].remove(x)
        liczba = bfs(H, s, t)
        leng -= 1
        p += 1
        if liczba > maxi:
            krotka = u
            break
    return krotka


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )