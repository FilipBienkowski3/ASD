def bubbleSortR(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n - i - 1):
            if T[j] > T[j + 1]:#
                T[j], T[j + 1] = T[j + 1], T[j]
    return T

def bubbleSortM(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n - i - 1):
            if T[j] < T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T
def bubbleSortT(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n - i - 1):
            if T[j][1] > T[j + 1][1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T

T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
T2 = [(2, 1), (3, 0), (-1, 2)]

print(bubbleSortM(T))
print(bubbleSortR(T))
print(bubbleSortT(T2))