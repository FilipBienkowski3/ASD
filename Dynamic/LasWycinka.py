T=[2,3,6,6,-1,2]
f= [-1 for i in range(len(T))]
print(f)
for i in range(len(T)):
  if i ==0:
    f[i]=T[i]
    continue
  if i==1:
    f[i]=max(T[i],T[i-1])
    continue
  f[i]=max(f[i-1],f[i-2]+T[i])#Wybieramy drzewo, przechodzimy 2 pola
print(f[len(T)-1])
print(f)