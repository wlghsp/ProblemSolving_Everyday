"""
-1은 공기청정기 1번 열이며 두 행 차지 위아래 차지

1. 미세먼지 확산
  모든 칸에서 동시에 일어남
  네 방향 확산, 공기청정기나 칸이 없으면 확산 X
  확산되는 양은 먼지/5 이고 소수점 버림.
  남은 미세먼지 양은 먼지 - [먼지/5] * 확산된 방향 갯수

2. 공기청정기 작동
  공기청정기 바람 나옴
  위쪽 반시계방향 순환, 아래쪽 시계방향 순환
  바람이 불면 미세먼지가 바람의 방향대로 모두 한칸 씩 이동
  공기청정기로 들어간 미세먼지는 모두 정화
"""
R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
upper_x = 0
for i in range(R):
    if grid[i][0] == -1 and grid[i + 1][0] == -1:
        upper_x = i

def get_dusk():
    result = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != -1 and grid[i][j] != 0:
                result.append((i, j))
    return result

def spread_dusk(dusk):
    for x, y in dusk:
        cnt = 0
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C): continue
            if grid[nx][ny] == -1: continue

            grid[nx][ny] += grid[x][y] // 5
            cnt += 1

        grid[x][y] -= grid[x][y] // 5 * cnt


def operate_purifier():
    pass

for _ in range(T):
    # 1. 미세먼지 확산
    dusk_locs = get_dusk()
    spread_dusk(dusk_locs)

    # 2. 공기청정기 작동
    operate_purifier()

print(sum(sum(row) for row in grid) + 2)