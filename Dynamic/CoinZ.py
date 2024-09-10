def change(T,C):
  F=[float('inf') for _ in range(T+1)]
  F[0]=0
  for i in range(1,T+1):
    for c in C:
      cast=F[i-c]+1 if i-c>=0 else float('inf')
      if F[i]>cast:
        F[i]=cast
  return F[T]



def changeZ(T,C):
  licznik=0
  for i in range(len(T)-1,-1,-1):
    if C==0:
      return licznik
    while T[i]>C:
      C-=T[i]
      licznik+=1
  return licznik
C2=[16,8,8,4,2,2,1]
C=[1,5,8]
T=17
T2=27
print(change(T2,C2))
print(change(T2,C2))


