def insertionSort_dobucketaM(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] < up:#
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSortM(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
    for j in x:
        index_b = slot_num-1 -int(slot_num * j)
        arr[index_b].append(j)
    for i in range(slot_num):
        arr[i] = insertionSort_dobucketaM(arr[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x



def insertionSort_dobucketaR(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b
def bucketSortR(T):
  maxlen=0
  for el in T:
    maxlen=max(maxlen,el//10)#ew zmiany
  buckets=[[] for _ in range(maxlen+1,0,-1)]
  for el in T:
    buckets[el//10].append(el)#ew zmiany
  for i in range(maxlen,-1,-1):#rosnaco czy malejaco
    buckets[i]=insertionSort_dobucketaR(buckets[i])
  o=0
  # for j in range(maxlen,-1,-1):#ewntualnie scalamy czasem potrzebujemy tylko jednego bucketa i np tylko jego ortujemy
  for j in range(maxlen+1):
    for k in range(len(buckets[j])):
      T[o]=buckets[j][k]
      o+=1
  return T

T = [52, 12, 43, 22, 83,36,24,55,26,7,43,84,23,1045,65,75,57,37,73,6,21]
T2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
print(bucketSortR(T))

print(bucketSortM(T2))
