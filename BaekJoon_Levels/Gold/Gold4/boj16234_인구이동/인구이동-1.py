import sys

sys.setrecursionlimit(10 ** 6)
N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
locs = [(a, b) for a in range(N) for b in range(N)]
unions = {}
can_move = False
total_population = 0
union_cnt = 0
team = []

def check_open_close():
    global can_move

    for r in range(N):
        for c in range(N):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dx, c + dy
                if not (0 <= nr < N and 0 <= nc < N): continue

                if L <= abs(population[r][c] - population[nr][nc]) <= R:
                    unions[(r, c)].append((nr, nc))
                    unions[(nr, nc)].append((r, c))
                    can_move = True

def dfs(x, y):
    global total_population, union_cnt

    visited[x][y] = True
    team.append((x, y))
    union_cnt += 1
    total_population += population[x][y]

    for nx, ny in unions[(x, y)]:
        if not visited[nx][ny]:
            dfs(nx, ny)

days = 0
while True:
    can_move = False
    unions = {(r, c): [] for r in range(N) for c in range(N)}
    # 1. 각 나라간 확인하여 인접리스트 처리
    check_open_close()

    if not can_move:
        break

    # 2. 열린 경우 탐색해서 갯수와 인구수 총합 구하고 각 칸을 채운다
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and len(unions[(i, j)]) >= 1:
                total_population, union_cnt = 0, 0
                team = []
                dfs(i, j)

                each_population = total_population // union_cnt
                for r, c in team:
                    population[r][c] = each_population

    days += 1

print(days)
