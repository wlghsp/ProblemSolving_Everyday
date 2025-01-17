import sys

sys.setrecursionlimit(10 ** 6)

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    square_map = [list(input().split()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    def dfs(x, y):
        visited[x][y] = True

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W: continue
            if square_map[nx][ny] == '0': continue
            if visited[nx][ny]: continue

            dfs(nx, ny)

    cnt = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and square_map[i][j] == '1':
                cnt += 1
                dfs(i, j)
    print(cnt)