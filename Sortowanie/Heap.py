def heapifyR(T, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and T[largest] < T[l]:#
        largest = l
    if r < n and T[largest] < T[r]:#
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapifyR(T, n, largest)

def heapSortR(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        heapifyR(T, n, i)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapifyR(T, i, 0)


def heapifyM(T, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and T[smallest] > T[l]:#
        smallest = l
    if r < n and T[smallest] > T[r]:#
        smallest = r
    if smallest != i:
        T[i], T[smallest] = T[smallest], T[i]
        heapifyM(T, n, smallest)

def heapSortM(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        heapifyM(T, n, i)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapifyM(T, i, 0)


def heapifyT(T, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and T[smallest][1] > T[l][1]:#
        smallest = l
    if r < n and T[smallest][1] > T[r][1]:#
        smallest = r
    if smallest != i:
        T[i], T[smallest] = T[smallest], T[i]
        heapifyT(T, n, smallest)

def heapSortT(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        heapifyT(T, n, i)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapifyT(T, i, 0)


T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

heapSortM(T)
print(T)

heapSortR(T)
print(T)

heapSortT(T2)
print(T2)
