#Filip Bieńkowski
#algorytm polega zastąpieniu wejściowej tablicy M, listą sąsiedztwa G z dodanymi nowymi n+ 2 wierzchołkami.
#n pierwotnych wierzchołków reprezentujące pracowników, których łacze odpowiednio z n nowymi wierzchołkami reprezentujących maszyny na którch mogą pracować.
#pozostałe 2 nowe wierchołki są wejściem i ujściem odpowiednio połaczone z innymi tworzą graf dwudzielny, który w połaczeniu z algorytem Forda Fulkersona pozwala znaleźć rozwiązenie,
#znajdując maksymalne skojarzenie uzyskujemy najlepsze przyporządkowanie pracowników do maszyn.
#by algortym dzialał poprawinie kazda krawedz powinna mieć wage 1, problem ten sprowadza sie do usuwania krawędzi z otrzymanej ścieżki oraz do dodawania przeciwnych.
#Złożoność czasowa to O(EF), gdzie F to wartość najlepszego przepływu.
from zad6testy import runtests
from copy import deepcopy
from collections import deque


def BFS(G, s, t):
    n = len(G)
    parent = [None for i in range(n)]
    q = deque()
    q.appendleft(s)
    while q and parent[t] == None:
        v = q.popleft()
        for u in G[v]:
            if parent[u] == None:
                q.appendleft(u)
                parent[u] = v
    if parent[t] == None:
        return
    path = [t]
    x = t
    while x != s:
        x = parent[x]
        path.append(x)
    return path[::-1]


def update(G, path):
    n = len(path)
    for i in range(n - 1):
        G[path[i + 1]].append(path[i])
        G[path[i]].remove(path[i + 1])


def ff(G, s, t):
    flow = 0
    G2 = deepcopy(G)
    path = BFS(G2, s, t)
    while path:
        flow += 1
        update(G2, path)
        path = BFS(G2, s, t)
    return flow


def binworker( M ):
    n = len(M)
    G = [[] for _ in range(2 * n + 2)]
    for i in range(n):
        for el in M[i]:
            G[i].append(n + el)
    for i in range(n):
        G[2 * n].append(i)
    for i in range(n, 2 * n):
        G[i].append(2 * n + 1)
    return ff(G, 2 * n, 2 * n + 1)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
