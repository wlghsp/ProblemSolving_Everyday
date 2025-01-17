import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(T):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    def dfs(x, y):
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if field[nx][ny] == 0: continue
            if visited[nx][ny]: continue

            dfs(nx, ny)

    cnt = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and field[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)