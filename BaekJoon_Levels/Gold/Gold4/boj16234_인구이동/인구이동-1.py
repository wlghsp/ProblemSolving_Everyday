N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
locs = [(a, b) for a in range(N) for b in range(N)]
loc_dict = {i: (l[0], l[1]) for i, l in zip(range(1, N * N + 1), locs)}
unions = []
can_move = False
def check_open_close(picked, start):
    global can_move
    if len(picked) == 2:
        # 확인하고 개방하면 인접리스트 처리
        x, y = loc_dict[picked[0]]
        r, c = loc_dict[picked[1]]
        if L <= abs(population[x][y] - population[r][c]) <= R:
            unions[picked[0]].append(picked[1])
            unions[picked[1]].append(picked[0])
            can_move = True
        return
    for i in range(start, N * N + 1):
        if i in picked: continue

        check_open_close(picked + [i], i + 1)

days = 0
while True:
    can_move = False
    unions = [[] * (N * N + 1)]
    # 1. 각 나라간 확인하여 인접리스트 처리
    check_open_close([], 1)

    if can_move:
        # 2. 열린 경우 탐색해서 갯수와 인구수 총합 구하고 각 칸을 채운다
        visited = [False] * (N * N + 1)
        for i in range(1, N * N + 1):
            if not visited[i] and len(unions[i]) >= 2:
                visited[i] = True
                total, cnt = 0, len(unions[i])
                for c in unions[i]:
                    visited[c] = True
                    x, y = loc_dict[c]
                    total += population[x][y]
                each_population = total // cnt
                for c in unions[i]:
                    x, y = loc_dict[c]
                    population[x][y] = each_population

        days += 1
    else:
        break

print(days)
