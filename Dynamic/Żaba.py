def hungry_frog(T):
    n = len(T)
    to_end = [float('inf') for _ in range(n)]
    to_end[n - 1] = 0

    for i in range(n - 2, -1, -1):
        for j in range(T[i], 0, -1):
            if i + j < n and to_end[i + j] + 1 < to_end[i]:
                to_end[i] = to_end[i + j] + 1

    return to_end[0]


T1 = [3, 1, 2, 2, 0, 0]
T = [5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
print(hungry_frog(T1))