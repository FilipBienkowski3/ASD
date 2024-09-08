def select(T, low,key, high):
    if low < high:
        pi = partition(T, low, high)
        if pi <key:
          select(T, pi+1,key, high)
        elif pi>key:
          select(T, low, key,pi-1)

def partition(T, low, high):
    pivot = T[high]#T[j][1]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:#< T[j][1]
            i = i + 1
            (T[i], T[j]) = (T[j], T[i])
    (T[i + 1], T[high]) = (T[high], T[i + 1])
    return i + 1

arr = [0,4,5,2,1,5,76,9,4,1,2,3,4,7,3,7,5]

select(arr,0,7,len(arr)-1)
print(arr)