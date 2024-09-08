def partitionM(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] >= pivot:
            i = i + 1
            (T[i], T[j]) = (T[j], T[i])
    (T[i + 1], T[high]) = (T[high], T[i + 1])
    return i + 1


def quickSortM(T, low, high):
    if low < high:
        pi = partitionM(T, low, high)
        quickSortM(T, low, pi - 1)
        quickSortM(T, pi + 1, high)


def partitionR(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i = i + 1
            (T[i], T[j]) = (T[j], T[i])
    (T[i + 1], T[high]) = (T[high], T[i + 1])
    return i + 1


def quickSortR(T, low, high):
    if low < high:
        pi = partitionR(T, low, high)
        quickSortR(T, low, pi - 1)
        quickSortR(T, pi + 1, high)


def partitionT(T, low, high):
    pivot = T[high][1]
    i = low - 1
    for j in range(low, high):
        if T[j][1] <= pivot:
            i = i + 1
            (T[i], T[j]) = (T[j], T[i])
    (T[i + 1], T[high]) = (T[high], T[i + 1])
    return i + 1


def quickSortT(T, low, high):
    if low < high:
        pi = partitionT(T, low, high)
        quickSortT(T, low, pi - 1)
        quickSortT(T, pi + 1, high)


T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

quickSortM(T, 0, len(T) - 1)
print("Sortowanie malejące:", T)

quickSortR(T, 0, len(T) - 1)
print("Sortowanie rosnące:", T)

quickSortT(T2, 0, len(T2) - 1)
print("Sortowanie tupli według drugiego elementu:", T2)