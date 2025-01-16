from collections import deque

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

distances = [[-1] * M for _ in range(N)]

dq = deque()

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            dq.append([i, j])
            distances[i][j] = 0

while dq:
    px, py = dq.popleft()

    for i in range(8):
        nx, ny = px + dx[i], py + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if distances[nx][ny] != -1: continue
        if space[nx][ny] == 1: continue

        distances[nx][ny] = distances[px][py] + 1
        dq.append([nx, ny])

max_distance = max(max(row) for row in distances)
print(max_distance)