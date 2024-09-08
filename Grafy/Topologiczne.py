#Tylko dla skierowanych, acykliczny graf
#Wykonywanie zadan w jakies kolejnosci wiedzac ze niektore maja byc przed innymi
def dfs_rec(v, vis, G, posortowane):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            dfs_rec(u, vis, G, posortowane)
    posortowane.append(v)


def sortowanie(G):
  n = len(G)
  vis = [False for _ in range(n)]
  posortowowane = []
  for v in range(n):
    if not vis[v]:
      dfs_rec(v, vis, G, posortowowane)
  return  posortowowane[::-1]

H=[[1,2],[2,4],[],[],[3,6],[4],[]]
G = [[1, 3], [2, 4], [], [1, 2], [2]]
print(sortowanie(G))