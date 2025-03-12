import copy
from collections import deque

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
upper_x, bottom_x = 0, 0

for i in range(R):
    if grid[i][0] == -1 and grid[i + 1][0] == -1:
        upper_x, bottom_x = i, i + 1
def get_dusk_locs():
    result = deque()
    for i in range(R):
        for j in range(C):
            if grid[i][j] >= 5:
                result.append((i, j, int(grid[i][j] / 5)))
    return result

def spread_dusk(dusk_locs):
    while dusk_locs:
        x, y, spread_amount = dusk_locs.popleft()
        cnt = 0
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C): continue
            if grid[nx][ny] < 0: continue

            grid[nx][ny] += spread_amount
            cnt += 1
        grid[x][y] -= spread_amount * cnt
        if grid[x][y] < 0:
            grid[x][y] = 0

def operate_purifier():
    # 1. 위쪽 공기청정기 가동
    grid[upper_x - 1][0] = 0
    for i in range(upper_x - 2, -1, -1):
        grid[i + 1][0] = grid[i][0]
        grid[i][0] = 0
    for i in range(1, C):
        grid[0][i - 1] = grid[0][i]
        grid[0][i] = 0
    for i in range(1, upper_x + 1):
        grid[i - 1][C - 1] = grid[i][C - 1]
        grid[i][C - 1] = 0
    for i in range(C - 2, 0, -1):
        grid[upper_x][i + 1] = grid[upper_x][i]
        grid[upper_x][i] = 0

    # 2. 아래쪽 공기청정기 가동
    grid[bottom_x + 1][0] = 0
    for i in range(bottom_x + 2, R):
        grid[i - 1][0] = grid[i][0]
        grid[i][0] = 0
    for i in range(1, C):
        grid[R - 1][i - 1] = grid[R - 1][i]
        grid[R - 1][i] = 0
    for i in range(R - 2, bottom_x - 1, -1):
        grid[i + 1][C - 1] = grid[i][C - 1]
        grid[i][C - 1] = 0
    for i in range(C - 2, 0, -1):
        grid[bottom_x][i + 1] = grid[bottom_x][i]
        grid[bottom_x][i] = 0

for _ in range(T):
    # 1. 미세먼지 확산
    locs = get_dusk_locs()
    spread_dusk(locs)

    # 2. 공기청정기 작동
    operate_purifier()

print(sum(sum(row) for row in grid) + 2)
