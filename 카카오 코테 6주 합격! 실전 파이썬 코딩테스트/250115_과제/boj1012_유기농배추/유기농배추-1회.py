import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(field, n, m, x, y):
    field[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
        if field[nx][ny] == 0: continue

        dfs(field, n, m, nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    cnt = 0


    def dfs(x, y):
        field[x][y] = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
            if field[nx][ny] == 0: continue

            dfs(nx, ny)

    for i in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)