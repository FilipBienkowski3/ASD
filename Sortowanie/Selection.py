def selectionSortM(T):
    n = len(T)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if T[max_idx] < T[j]:
                max_idx = j
        T[i], T[max_idx] = T[max_idx], T[i]
    return T


def selectionSortR(T):
    n = len(T)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if T[min_idx] > T[j]:
                min_idx = j
        T[i], T[min_idx] = T[min_idx], T[i]
    return T

def selectionSortT(T):
    n = len(T)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if T[min_idx][1] > T[j][1]:
                min_idx = j
        T[i], T[min_idx] = T[min_idx], T[i]
    return T


T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

print(selectionSortM(T))
print(selectionSortR(T))
print(selectionSortT(T2))
