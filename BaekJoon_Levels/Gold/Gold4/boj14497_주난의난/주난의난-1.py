from collections import deque

N, M = map(int, input().split()) # 교실 크기 N, M
x1, y1, x2, y2 = map(int, input().split()) # 주난이의 위치 (x1, y1), 범인의 위치 (x2, y2)
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
room = [list(input()) for _ in range(N)]


def bfs():
    dist = [[-1] * M for _ in range(N)]
    q = deque([(x1, y1)])
    dist[x1][y1] = 0

    while q:
        px, py = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = px + dx, py + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if dist[nx][ny] == -1: continue

            room[nx][ny] = 0
            dist[nx][ny] = dist[px][py] + 1
            q.append((nx, ny))
    print(*dist, sep='\n')
bfs()
