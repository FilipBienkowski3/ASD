def countSortR(A):
    k = max(A) + 1
    n=len(A)
    C=[0]*k
    B = [0] * n
    for i in range(n):
        C[A[i]]+=1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    for i in range(n):
        A[i]=B[i]
    return A

def countSortM(A):
    k = max(A) + 1
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(n):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[n - 1 - i]
    return A



T = [52, 12, 43, 22, 83, 36, 24, 55, 26, 7, 43, 84, 23, 65, 75, 57, 37, 73]
#Trzeba podać zakres liczb
print(countSortM(T))
print(countSortR(T))
