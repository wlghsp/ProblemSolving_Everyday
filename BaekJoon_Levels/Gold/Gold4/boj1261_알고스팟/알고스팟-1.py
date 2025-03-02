from collections import deque

M, N = map(int, input().split())
maze = [list(input()) for _ in range(N)]

def bfs():
    dist = [[-1] * M for _ in range(N)]
    q = deque([(0, 0)])
    dist[0][0] = 0
    while q:
        px, py = q.popleft()

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = px + dx, py + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if dist[nx][ny] != -1: continue

            if maze[nx][ny] == '0':
                dist[nx][ny] = dist[px][py]
                q.appendleft((nx, ny))
            else:
                dist[nx][ny] = dist[px][py] + 1
                q.append((nx, ny))

    return dist[N - 1][M - 1]
print(bfs())