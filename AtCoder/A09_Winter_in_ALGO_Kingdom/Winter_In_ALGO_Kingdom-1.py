H, W, N = map(int, input().split())
grid = [[0] * (W + 2) for _ in range(H + 2)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    grid[A][B] += 1
    grid[A][D + 1] -= 1
    grid[C + 1][B] -= 1
    grid[C + 1][D + 1] += 1


for i in range(1, H + 1):
    for j in range(1, W + 1):
        grid[i][j] += grid[i][j - 1]
for j in range(1, W + 1):
    for i in range(1, H + 1):
        grid[i][j] += grid[i - 1][j]

for row in grid[1:H+1]:
    print(*row[1:W+1], sep=' ')
