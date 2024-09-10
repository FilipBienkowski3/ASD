def klocki(T, cache, top, i):
    if i == 0:
        top[0] = T[0]
        return 0
    if cache[i] != -1:
        return cache[i]
    cache[i] = min(klocki(T, cache, top, i - 1) + 1,
                   min([klocki(T, cache, top, j) + (i - j + 1) for j in range(i) if upper(T[i], top[j])]),
                   i)
    if cache[i] == (klocki(T, cache, top, i - 1) + 1):
        top[i] = top[i - 1]
    else:
        top[i] = T[i]
    return cache[i]


def upper(a, b):
    if a[0] < b[0] or a[1] > b[1]:
        return False
    return True


def klockii(T, n):
    cache = [-1 for i in range(n)]
    top = [None for i in range(n)]
    cache[0] = 0
    top[0] = T[0]
    return klocki(T, cache, top, n)
