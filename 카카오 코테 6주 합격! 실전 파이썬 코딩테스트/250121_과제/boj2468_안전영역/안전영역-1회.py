import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * N for _ in range(N)]

max_height = 0
max_safe_area_cnt = 1 # 아무 지역도 물에 잠기지 않으면 1
for i in range(N):
    for j in range(N):
        max_height = max(max_height, area[i][j])

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
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and area[x][y] > max_h:
                cnt += 1
                dfs(x, y, max_h)
    return cnt

# 높이 1 ~ 최대 높이 - 1 까지 시도
for i in range(1, max_height):
    max_safe_area_cnt = max(max_safe_area_cnt, get_safe_area_cnt(i))
    visited = [[False] * N for _ in range(N)]

print(max_safe_area_cnt)