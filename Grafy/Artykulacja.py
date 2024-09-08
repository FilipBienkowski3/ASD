def DFS(G,ban):
  n=len(G)
  visited=[False for i in range(n)]
  counter=0
  def DFSvisit(G,u):
    nonlocal visited
    visited[u]=True
    for v in G[u]:
      if v!=ban:
        if not visited[v]:
          DFSvisit(G,v)
  for u in range(n):
    if u!=ban:
      if not visited[u]:
        DFSvisit(G,u)
        counter+=1
  return counter
  
def artikulacja(G):
  artyk=[]
  for i in range(len(G)):
    if DFS(G,i)>=2:
      artyk.append(i)
  return artyk
G=[[1,2],[0,2],[3],[4],[]]
print(artikulacja(G))



