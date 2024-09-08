#Czy istnieje cykl
#skierowany
def DFScycle(G):
  n = len(G)
  visited = [False for i in range(n)]
  recStack = [False for i in range(n)]
  def DFSvisitcycle(G, u):
    visited[u] = True
    recStack[u]=True
    for v in G[u]:
      if not visited[v]:
        if DFSvisitcycle(G,v):
          return True
      elif recStack[v]==True:
        return True
    recStack[u]=False
    return False

  for u in range(n):
    if not visited[u]:
      if DFSvisitcycle(G, u):
        return True
    
  return False

G=[[1,2],[0,2],[0,1]]
G1=[[1],[2,0],[]]
G2=[[2],[2],[3],[]]
print(DFScycle(G))
print(DFScycle(G1))
print(DFScycle(G2))



