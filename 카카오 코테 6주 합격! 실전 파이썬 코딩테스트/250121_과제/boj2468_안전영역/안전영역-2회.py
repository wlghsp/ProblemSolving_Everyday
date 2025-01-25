import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_height = max(max(row) for row in area)
visited = [[False] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_safe_area_cnt = 1

def dfs(x, y, max_h):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visited[nx][ny]: continue
        if area[nx][ny] <= max_h: continue

        dfs(nx, ny, max_h)

def get_safe_area_cnt(max_h):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > max_h:
                cnt += 1
                dfs(i, j, max_h)
    return cnt

for i in range(1, max_height):
    max_safe_area_cnt = max(max_safe_area_cnt, get_safe_area_cnt(i))
    visited = [[False] * N for _ in range(N)]

print(max_safe_area_cnt)