import sys

sys.setrecursionlimit(10 ** 6)

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[False] * w for _ in range(h)]
    square_map = [list(map(int, input().split())) for _ in range(h)]

    def dfs(x, y):
        visited[x][y] = True

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if visited[nx][ny]: continue
            if square_map[nx][ny] == 0: continue

            dfs(nx, ny)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and square_map[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)

