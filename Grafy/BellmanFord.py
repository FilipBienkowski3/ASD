#djkstra dla ujemnych wag
#najkrotsza sciezka
#skierwany wazony graf
#nie moze posiadac ujemnych cykli


def bellmanford(G,s):
  inf=float("inf")
  maxedge = max(G, key=lambda x: max(x[0], x[1]))
  n = max(maxedge[0], maxedge[1]) + 1
  V=n
  distance=[inf]*n
  parent=[None]*n
  distance[s]=0
  for i in range(V-1):
    for u,v,w in G:
      if distance[u] != float("Inf") and distance[u] + w < distance[v]:
        distance[v] = distance[u] + w
        parent[v]=u
  for u, v, w in G:
    if distance[u] != float("Inf") and distance[u] + w < distance[v]:
      print("Graph contains negative weight cycle")
      return
  return distance,parent

g=[(0, 1, -1),(0, 2, 4),(1, 2, 3),(1, 3, 2),(1, 4, 2),(3, 2, 5),(3, 1, 1),(4, 3, -3)]
  
print(bellmanford(g,0))
