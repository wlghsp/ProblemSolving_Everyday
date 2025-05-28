import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if maze[nx][ny] == '0': continue
            if dist[nx][ny] != -1: continue

            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    return dist[N - 1][M - 1]

print(bfs())