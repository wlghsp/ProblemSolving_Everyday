
N = int(input())
grid = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    grid[A][B] += 1
    grid[A][D] -= 1
    grid[C][B] -= 1
    grid[C][D] += 1

for i in range(1501):
    for j in range(1, 1501):
        grid[i][j] += grid[i][j - 1]

for j in range(1501):
    for i in range(1, 1501):
        grid[i][j] += grid[i - 1][j]
ans = 0
for i in range(1501):
    for j in range(1501):
        if grid[i][j] > 0:
            ans += 1

print(ans)