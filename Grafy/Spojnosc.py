#sprawdzanie spojnosci 1-spójny
def DFS(G):
  n=len(G)
  visited=[False for i in range(n)]
  counter=0
  def DFSvisit(G,u):
    nonlocal visited
    visited[u]=True
    for v in G[u]:
      if not visited[v]:
        DFSvisit(G,v)
  for u in range(n):
    if not visited[u]:
      DFSvisit(G,u)
      counter+=1
  return counter
G=[[1],[2],[3],[4],[]]
print(DFS(G))
