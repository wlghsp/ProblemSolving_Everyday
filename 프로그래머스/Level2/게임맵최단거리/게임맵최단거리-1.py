from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1] * m for _ in range(n)]
    q = deque([(0, 0)])
    dist[0][0] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if maps[nx][ny] == 0: continue
            if dist[nx][ny] != -1: continue

            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

    return dist[n - 1][m - 1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
