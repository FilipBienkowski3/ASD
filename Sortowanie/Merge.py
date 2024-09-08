def mergeSortM(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        mergeSortM(L)
        mergeSortM(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] >= R[j]:#
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
    return T

def mergeSortR(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        mergeSortR(L)
        mergeSortR(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:##
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
    return T


def mergeSortT(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        mergeSortT(L)
        mergeSortT(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] <= R[j][1]:##
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
    return T
T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

print(mergeSortM(T))
print(mergeSortR(T))
print(mergeSortT(T2))
