def przedzialy(P):#lista punktow
  P.sort()
  licznik=0
  while P:
    start=P[0]
    while start<=P[0] <=start+1:
      P.pop()
    licznik+=1
  return licznik