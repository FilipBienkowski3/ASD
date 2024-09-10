def f(T,DP,a,b):
  if a==b:
    return T[a]
  if DP[a][b]!=-1:
    return DP[a][b]
  DP[a][b]=min(f(T,DP,a,b-1),T[b])
  return DP[a][b]
T=[2,5,5,98,3,7]
DP=[[-1 for _ in range(len(T))] for _ in range(len(T))]
print(f(T,DP,1,5))

#max
def f(T,DP,a,b):
  if a==b:
    return T[a]
  if DP[a][b]!=-1:
    return DP[a][b]
  DP[a][b]=max(f(T,DP,a,b-1),T[b])
  return DP[a][b]
T=[2,5,5,98,3,7]
DP=[[-1 for _ in range(len(T))] for _ in range(len(T))]
print(f(T,DP,1,5))