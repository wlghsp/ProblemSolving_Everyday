import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
empty_spaces = []
viruses = []
v_map = None
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            empty_spaces.append((i, j))
        elif laboratory[i][j] == 2:
            viruses.append((i, j))
combs = combinations(empty_spaces, 3)
max_area = 0

def get_area_cnt():
    area = 0
    for i in range(N):
        for j in range(M):
            if v_map[i][j] == 0:
                area += 1
    return area

def dfs(x, y):
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if v_map[nx][ny] != 0: continue

        v_map[nx][ny] = 2
        dfs(nx, ny)

def spread_virus():
    for x, y in viruses:
        dfs(x, y)

for comb in combs:
    for x,y in comb:
        laboratory[x][y] = 1

    v_map = [row[:] for row in laboratory]
    spread_virus()
    max_area = max(max_area, get_area_cnt())

    for x,y in comb:
        laboratory[x][y] = 0

print(max_area)