# O(V2)MACIERZ E+VLISTOWA bfs tez
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



#skierowany
def DFSkl(G):
  n = len(G)
  visited = [False for i in range(n)]
  parent=[None for _ in range(n)]
  time = 0
  timi=[None for _ in range(n)]
  
  def DFSvisitkl(G, u):
    nonlocal time
    visited[u] = True
    timi[u]=time
    time+=1
    for v in G[u]:
      if not visited[v]:
        parent[v]=u
        DFSvisitkl(G, v)
  
  for u in range(n):
    if not visited[u]:
      DFSvisitkl(G, u)
      #time += 1#?
  return time, parent, visited,timi




def DFSpath(G,s,t):
  n = len(G)
  visited = [False for i in range(n)]
  counter = 0
  parent=[None for _ in range(n)]
  
  def DFSvisit(G, u):
    nonlocal visited
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        parent[v]=u
        DFSvisit(G, v)

  for u in range(n):
    if not visited[u] and parent[t]==None:
      DFSvisit(G, u)
      counter += 1
  if parent[t] == None:
      return
  path = [t]
  x = t
  while x != s:
    x = parent[x]
    path.append(x)
  return path[::-1]



def DFSmatrix(T,x,y):
  n = len(T)
  visited = [[False]*n for i in range(n)]
  add=0
  
  def DFSvisitmatrix(T, x1,y1):
    nonlocal add
    visited[x1][y1] = True
    add+=T[x1][y1]
    for (x2,y2) in [(x1-1,y1),(x1,y1+1),(x1+1,y1),(x1,y1-1)]:
      if 0<=x2 and x2<=n-1 and 0<=y2 and y2<=n-1:
        if visited[x2][y2]==False:
          if T[x2][y2]!=0:
            DFSvisitmatrix(T,x2,y2)
          
  for x1,y1 in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
    if 0<=x1 and x1<=n-1 and 0<=y1 and y1<=n-1:
      if visited[x1][y1]==False:
        if T[x1][y1]!=0:
          DFSvisitmatrix(T,x1,y1)
  return add


G2=[[1,2],[2,4],[],[],[3,6],[4],[]]

G3=[
  [1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]
]
T=[[3,0,0],
   [4,2,1],
   [0,0,0]]
print(DFSkl(G2))
print(DFSmatrix(T,0,0))
print(DFSpath(G2,0,6))
