def path(C):
  n = len(C)
  F = [[float('inf')] * n for _ in range(n)]
  F[n-1][n-1] = 0

  for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
      if i == n-1 and j == n-1:
        continue
      else:
        right = F[i+1][j] + C[i+1][j] if i+1 < n else float('inf')
        down = F[i][j+1] + C[i][j+1] if j+1 < n else float('inf')
        F[i][j] = min(right, down)

  return F[0][0]

C = [[1, 2, 4], [2, 2, 6], [1, 3, 3]]
print(path(C))