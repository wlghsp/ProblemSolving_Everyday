from collections import deque


def solution(maps):
    points = get_points(maps)
    s_to_l = bfs(points[0], points[1], maps)
    if s_to_l == -1:
        return -1
    l_to_e = bfs(points[1], points[2], maps)
    if l_to_e == -1:
        return -1
    return s_to_l + l_to_e


def bfs(start, target, maps):
    N, M = len(maps), len(maps[0])
    dist = [[-1] * M for _ in range(N)]
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([start])
    dist[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        if target == (x, y):
            return dist[x][y]

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if maps[nx][ny] == 'X': continue
            if dist[nx][ny] != -1: continue

            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

    return -1


def get_points(maps):
    S = L = E = None
    for i, row in enumerate(maps):
        for j, val in enumerate(row):
            if val == 'S':
                S = (i, j)
            elif val == 'L':
                L = (i, j)
            elif val == 'E':
                E = (i, j)
    return [S, L, E]


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))  # 16
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))  # -1
