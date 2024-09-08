#znajdowanie takich zbiorow wierzcholkow, miedzy kazda para istieje sciezka skierowana dotyczny grafow skierowanych



#da nam liczbe
def DFS(G):
  n = len(G)
  visited = [False for i in range(n)]
  counter = 0

  def DFSvisit(G, u):
    nonlocal visited
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        DFSvisit(G, v)

  for u in range(n):
    if not visited[u]:
      DFSvisit(G, u)
      counter += 1
  return counter

G = [
    [1],
    [0,2],
    [1]  ,[] ]
    
print(DFS(G))



#Znajduje zbiory wierzchołków

def DFSkl(G):
    n = len(G)
    stack = []
    visited = [False for i in range(n)]
    sccs = []

    def dfsutil(G, v, scc):
        nonlocal visitedd
        visitedd[v] = True
        scc.append(v)
        for i in G[v]:
            if not visitedd[i]:
                dfsutil(G, i, scc)

    def fillorderr(G, u):
        nonlocal visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                fillorderr(G, v)
        stack.append(u)

    def transpoze(G):
        G2 = [[] for _ in range(len(G))]
        for i in range(n):
            for el in G[i]:
                G2[el].append(i)
        return G2

    for u in range(n):
        if not visited[u]:
            fillorderr(G, u)

    transG = transpoze(G)

    visitedd = [False for i in range(n)]

    
    while stack:
        i = stack.pop()
        if not visitedd[i]:
            scc = []
            dfsutil(transG, i, scc)
            sccs.append(scc)

    return sccs
G = [[2, 3], [0], [1], [4], []]

sccs = DFSkl(G)
print("Silnie spójne składowe:", sccs)
