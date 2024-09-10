def task(T):
  T.sort(key=lambda x: x[0])
  T.reverse()
  licznik = 0
  for i in range(5, -1, -1):
    maxi = 0
    poz = 0
    for j in range(len(T)):
      if T[j][0] >= i:
        if maxi < T[j][1]:
          maxi = T[j][1]
          poz = j
    del T[poz]
    licznik += maxi
  return licznik

T = [(5, 10), (1, 1), (2, 9), (4, 7), (5, 5), (3, 3), (2, 4)]
print(task(T))