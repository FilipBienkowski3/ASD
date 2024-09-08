#Dla spójnych działa
from collections import deque
def isBipartite(G,s):
    n=len(G) 
    colors=[0 for i in range(n)]
    Q=deque()
    Q.append(s) 
    colors[s]=1
    while len(Q)>0:
        u=Q.popleft() 
        for v in G[u]:
            if colors[v]==0:
                colors[v]=-1*colors[u] 
                Q.append(v) 
            elif colors[u]==colors[v]:
                return False 

    return True

G=[[],[2,3],[1,3],[1,2]] 
G2=[[1],[2],[3],[],[]]
print(isBipartite(G,0))