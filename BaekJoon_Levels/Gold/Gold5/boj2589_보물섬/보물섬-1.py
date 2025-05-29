import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]

def bfs(x, y):
    distance = [[-1] * M for _ in range(N)]
    max_local = 0
    distance[x][y] = 0

    q = deque()
    q.append((x, y))

    while q:
        px, py = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = px + dx, py + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if distance[nx][ny] != -1: continue
            if treasure[nx][ny] == 'W': continue

            distance[nx][ny] = distance[px][py] + 1
            max_local = max(max_local, distance[nx][ny])
            q.append((nx, ny))

    return max_local

max_dist = 0
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'W': continue

        max_dist = max(max_dist, bfs(i, j))

print(max_dist)
