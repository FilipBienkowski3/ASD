from collections import deque
import queue
def bfs(G,s,t):
  n=len(G)
  number=[-1 for i in range(n)]
  number[s]=0
  Q=deque()
  Q.append(s)
  while Q and number[t]==-1:
    u=Q.popleft()
    for v in G[u]:
      if number[v]==-1:
        number[v]=number[u]+1
        Q.append(v)
  if number[t] == -1:
    return float('inf')
  return number[t]

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

def klasycznybfs(G,S):
  q=queue.Queue()
  n=len(G)
  visited=[False for _ in range(n)]
  parent=[None for _ in range(n)]
  d=[-1 for _ in range(n)]
  d[s]=0
  visited[s]=True
  parent[s]=None
  q.put(s)
  while  not q.empty() :
    u=q.get()
    for v in G[u]:
      if not visited[v]:
        visited[v]=True
        d[v]=d[u]+1
        parent[v]=u
        q.put(v)
  return parent , d , visited
G = [ [1, 2],
[0, 2, 3],
[0, 1],[4],[]]
s = 0
t = 4
print(BFS(G,s,t))
print(klasycznybfs(G,s))