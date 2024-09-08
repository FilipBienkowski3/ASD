#wazony,skierowany graf
#macierz posiada droge miedzy wierzcholkami algorytm pozwala znalezc najkrotsze mzoliwe sciezki 
# o n3
# to zadanie to szukanie cycklu o najmniejszej wadze czyli to sie sporwadza do tam i spowrotem
INF = float('inf')
  
def floyd_warshall(G):
  n = len(G)
  for i in range(n):
    for j in range(n):
      for k in range(n):
          G[j][k] = min(G[j][k], G[j][i] + G[i][k])


  return G

def solve(G):
  n = len(G)
  dis = floyd_warshall(G)
  ans = INF
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      ans = min(ans, dis[i][j] + dis[j][i])
  return ans
G = [
    [0, 3, INF, INF, INF],
    [INF, 0, 1, INF, INF],
    [INF, INF, 0, 7, INF],
    [2, INF, INF, 0, INF],
    [INF, INF, INF, 2, 0]
]
print(solve(G))