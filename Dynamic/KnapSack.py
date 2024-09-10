from math import inf


# 1.1
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
            if i == n and w == W:
                print(K)
    return K[n][W]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [1, 2, 3]
    W = 5
    n = len(profit)
    print(knapSack(W, weight, profit, n))


# 1.2

def f(S, W, P, n):
    DP = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for s in range(S + 1):
            if i == 0 or s == 0:
                DP[i][s] = 0
            elif W[i - 1] <= s:
                DP[i][s] = max(P[i - 1] + DP[i - 1][s - W[i - 1]], DP[i - 1][s])
            else:
                DP[i][s] = DP[i - 1][s]
    return DP[n][S]


profit = [60, 100, 120]
weight = [1, 2, 3]
W = 5
n = len(profit)
print(f(W, weight, profit, n))


# 2.1

def knap(DP, W, wt, val, i):
    if W < 0:
        return -inf
    if i >= len(wt):
        return 0
    if DP[i][W] != None:
        return DP[i][W]
    d1 = knap(DP, W - val[i], wt, val, i + 1) + wt[i]
    d2 = knap(DP, W, wt, val, i + 1)
    DP[i][W] = max(d1, d2)
    return DP[i][W]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [1, 2, 3]
    W = 5
    DP = [[None for _ in range(W + 1)] for _ in range(len(profit))]
    print(knap(DP, W, profit, weight, 0))

2.2


def f(DP, S, P, W, i):
    if S < 0:
        return -inf
    if i >= len(P):
        return 0
    if DP[i][S] != None:
        return DP[i][S]
    d1 = f(DP, S - W[i], P, W, i + 1) + P[i]
    d2 = f(DP, S, P, W, i + 1)
    DP[i][S] = max(d1, d2)
    return DP[i][S]


P = [60, 100, 120]
W = [1, 2, 3]
S = 5
DP = [[None for _ in range(S + 1)] for _ in range(len(P))]
print(f(DP, S, P, W, 0))




# 3.2


def f(DP, S, P, W, i):
    if S < W[i]:
        return -inf
    if i >= len(P):
        return 0
    if DP[i][S] != None:
        return DP[i][S]
    d = 0
    for j in range(i):
        d = max(d, f(DP, S - W[i], P, W, j))
    DP[i][S] = d + P[i]
    return DP[i][S]


P = [60, 100, 120, 0]
W = [1, 2, 3, 0]
S = 5
DP = [[None for _ in range(S + 1)] for _ in range(len(P))]
print(f(DP, S, P, W, len(W) - 1))


def knapsack(T, w, h):
    n = len(T)
    dp = [[-float('inf')] * (w + 1) for _ in range(h + 1)]
    dp[0][0] = 0

    for k in range(n):
        for i in range(h, -1, -1):
            for j in range(w, -1, -1):
                if dp[i][j] > -float('inf') and i + T[k][1] <= h and j + T[k][0] <= w:
                    dp[i + T[k][1]][j + T[k][0]] = max(dp[i + T[k][1]][j + T[k][0]], dp[i][j] + T[k][2])

    cost = -float('inf')
    for i in range(h + 1):
        for j in range(w + 1):
            cost = max(cost, dp[i][j])

    return cost


# (waga, wysokość, wartość)
T = [(2, 3, 10), (1, 1, 6), (3, 2, 7)]
w = 4
h = 4

print(knapsack(T, w, h))



