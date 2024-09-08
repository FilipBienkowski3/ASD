# znajdowania maksymalnego przepływu w sieci przepływowej,
# czyli maksymalnej ilości przepływu, jaka może przejść 
# przez sieć od źródła do ujścia, przy respektowaniu ograniczeń na przepustowość krawędzi

from collections import deque
from copy import deepcopy

def BFS(G, s, t):
    n = len(G)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    q = deque()
    q.append(s)
    visited[s] = True  
    while q and not visited[t]:
        v = q.popleft()
        for i in range(n):
            if G[v][i] > 0 and not visited[i]:
                q.append(i)
                visited[i] = True
                parent[i] = v
    if not visited[t]:
        return []
    path = [t]
    x = t
    while x != s:
        x = parent[x]
        path.append(x)
    return path[::-1]

def capacity(G, path):
    min_cap = float('inf')
    n = len(path)
    for i in range(n - 1):
        min_cap = min(G[path[i]][path[i + 1]], min_cap)
    return min_cap

def update(G, path):
    w = capacity(G, path)
    n = len(path)
    for i in range(n - 1):
        G[path[i]][path[i + 1]] -= w
        G[path[i + 1]][path[i]] += w

def ff(G, s, t):
    flow = 0
    G2 = deepcopy(G)
    path = BFS(G2, s, t)
    while path:
        flow += capacity(G2, path)
        update(G2, path)
        path = BFS(G2, s, t)
    return flow

graph = [
    [0, 10, 5, 0],
    [0, 0, 15, 10],
    [0, 0, 0, 5],
    [0, 0, 0, 0]
]

source = 0
sink = 3
print(ff(graph, source, sink))












# dla list sasiedztwa
from collections import deque
from copy import deepcopy

def BFS(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    q = deque()
    q.append(s)
    visited[s] = True
    while q and not visited[t]:
        v = q.popleft()
        for neighbor, capacity in G[v]:
            if not visited[neighbor] and capacity > 0:
                q.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = v
    if not visited[t]:
        return []
    path = [t]
    x = t
    while x != s:
        x = parent[x]
        path.append(x)
    return path[::-1]

def calculate_capacity(G, path):
    min_cap = float('inf')
    n = len(path)
    for i in range(n - 1):
        for neighbor, capacity in G[path[i]]:
            if neighbor == path[i + 1]:
                min_cap = min(capacity, min_cap)
                break
    return min_cap

def update(G, path):
    w = calculate_capacity(G, path)
    n = len(path)
    for i in range(n - 1):
        for j, (neighbor, capacity) in enumerate(G[path[i]]):
            if neighbor == path[i + 1]:
                G[path[i]][j] = (neighbor, capacity - w)
                break
        for j, (neighbor, capacity) in enumerate(G[path[i + 1]]):
            if neighbor == path[i]:
                G[path[i + 1]][j] = (neighbor, capacity + w)
                break

def ff(G, s, t):
    flow = 0
    G2 = deepcopy(G)
    path = BFS(G2, s, t)
    while path:
        flow += calculate_capacity(G2, path)
        update(G2, path)
        path = BFS(G2, s, t)
    return flow

g = [
    [(1, 10), (2, 5)],
    [(2, 15), (3, 10)],
    [(3, 5)],
    []
]

source = 0
sink = 3  
max_flow = ff(g, source, sink)
print(f"Maksymalny przepływ z wierzchołka {source} do wierzchołka {sink}: {max_flow}")
