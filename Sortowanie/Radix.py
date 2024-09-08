def countingSortR(A, k):
    n = len(A)
    B = [0] * (n)
    C = [0] * (10)
    for i in range(0, n):
        index = A[i] // k
        C[index % 10] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    i = n - 1
    while i >= 0:
        index = A[i] // k
        B[C[index % 10] - 1] = A[i]
        C[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(A)):
        A[i] = B[i]


def radixSortR(T):
    max1 = max(T)
    exp = 1
    while max1 / exp >= 1:
        countingSortR(T, exp)
        exp *= 10


D = [1100, 100, 0, 1111, 1101]
radixSortR(D)
print(D)