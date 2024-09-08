def insertionSortR(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def insertionSortM(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and key > T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T

def insertionSortT(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and key[1] < T[j][1]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

print(insertionSortM(T))
print(insertionSortR(T))
print(insertionSortT(T2))
