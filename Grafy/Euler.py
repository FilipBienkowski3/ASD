#wszystkie krawedzie uzyte, wierzcholki odwiedzane kilkukrotnie
#macierzowa ,nieskierowany, kazdy wiercholek parzysty stopien
def dfs_rec(e, G, path):
    n = len(G)
    for i in range(n):
        if G[e][i] == 1:
            G[e][i] = G[i][e] = 0
            dfs_rec(i, G, path)
    path.append(e )#+1?


def Euler(G):
    n = len(G)
    total = 0
    for i in range(n):
        total += sum(G[i])
        if total % 2 == 1:
            return False
    path = []
    dfs_rec(0, G, path)
    if total / 2 + 1 != len(path):
        return False
    return path[::-1]



#listowa nieskierowany
def dfs_rec2(e, G, path):
    n = len(G)
    for i in range(n):
      for u in G[i]:
        if u==e:
          G[u].remove(i)
          G[i].remove(u)
          dfs_rec2(i, G, path)
    path.append(e)#+1?


def Euler2(G):
    n = len(G)
    total = 0
    for i in range(n):
        total += len(G[i])
        if total % 2 == 1:
            return False
    path = []
    dfs_rec2(0, G, path)
    if total / 2 + 1 != len(path):
        return False
    return path[::-1]

#Macierzowa
G = [[0, 1, 1, 0, 0], 
     [1, 0, 1, 0, 0], 
     [1, 1, 0, 1, 1], 
     [0, 0, 1, 0, 1],
     [0, 0, 1, 1, 0]]
print(Euler(G))

#Listowa
G1=[[1,2],[0,2],[0,1,3,4],[2,4],[2,3]]
print(Euler2(G1))