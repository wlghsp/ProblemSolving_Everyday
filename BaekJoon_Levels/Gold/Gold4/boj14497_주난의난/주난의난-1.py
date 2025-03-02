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
            if not (0 <= nx < N and 0 <= ny < M): continue
            if dist[nx][ny] != -1: continue

            if room[nx][ny] == '0':
                dist[nx][ny] = dist[px][py]
                q.appendleft((nx, ny))
            else:
                dist[nx][ny] = dist[px][py] + 1
                q.append((nx, ny))

            if (nx, ny) == (x2, y2):
                return dist[nx][ny]
    return dist[x2][y2]
print(bfs())
