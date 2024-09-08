#nieskierowany, usuniecie krawedzi spowoduje ze stanie sie niespojny
#nie lezy na cyklu

         
def DFSbri(G):
  n = len(G)
  visited = [False for i in range(n)]
  disc=[None for i in range(n)]
  low=[None for _ in range(n)]
  parent=[-1 for _ in range(n)]
  time = 0
  mosty=[]
  
  def DFSvisitbri(G, u):
    nonlocal time
    visited[u] = True
    disc[u]=time
    low[u]=time
    time+=1
    for v in G[u]:
      if not visited[v]:
        parent[v]=u
        DFSvisitbri(G, v)
        low[u] = min(low[u], low[v])
        if low[v] > disc[u]:
          mosty.append([u,v])
      elif v != parent[u]:
        low[u] = min(low[u], disc[v])

  for u in range(n):
    if not visited[u]:
      DFSvisitbri(G, u)
  return mosty

G=[[1],[2],[3],[]]
G1=[[1,3],[0,2],[1,3,5],[0,2,4],[3],[2,6,7],[5,7],[5,6]]
print(DFSbri(G))

