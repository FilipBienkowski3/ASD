from math import inf
# T.sort(key=lambda x :(x[0],x[1]))
def f(T,DP,i):
  if i==0:
    return 1
  if DP[i]!=-1:
    return DP[i]
  maxi=1
  for j in range(i):
    if T[j]<T[i]:
      maxi=max(maxi,f(T,DP,j)+1)

  DP[i]=maxi
  return DP[i]
def lis(T):
  T.append(inf)
  DP=[-1 for _ in range(len(T))]
  return f(T,DP,len(T)-1)-1
T=[2,5,3,6,3,2,4]
print(lis(T))
