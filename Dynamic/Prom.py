#Ile maksymanie można zabrać pojazdów o długości z tablicy S na prom gdzie mogą wjeżdżać na lewy (l1) albo prawy parking (l2).
def rek(i,S,l1,l2):
  if l1 < 0 or l2 < 0:
    return -1
  return max(rek(i-1,S,l1-S[i],l2)+1,rek(i-1,S,l1,l2-S[i])+1)
l1 = 7
l2 = 4
S = [7,7]
print(rek(len(S)-1,S,l1,l2))
