from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
distances = [[-1] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    dq = deque([(x, y)])
    distances[x][y] = 1

    while dq:
        px, py = dq.popleft()

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if maze[nx][ny] != '1': continue
            if distances[nx][ny] != -1: continue

            distances[nx][ny] = distances[px][py] + 1
            dq.append((nx, ny))

bfs(0, 0)
print(distances[N - 1][M - 1])