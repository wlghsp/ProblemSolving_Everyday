N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, -1), (1, 0), (1, 1)]
min_cost = float('inf')
def dfs(x, y, prev_dir, cost):
    global min_cost

    if x == N - 1:
        min_cost = min(min_cost, cost)
        return

    for i in range(3):
        if prev_dir != -1 and i == prev_dir:
            continue
        nx, ny = x + dir[i][0], y + dir[i][1]
        if not (0 <= nx < N and 0 <= ny < M): continue

        dfs(nx, ny, i, cost + space[nx][ny])


for y in range(M):
    dfs(0, y, -1, space[0][y])

print(min_cost)