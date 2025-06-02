import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
maze = [list(input()) for _ in range(N)]

def bfs():
    visited = [[False] * M for _ in range(N)]
    q = deque([(N - 1, M - 1, 0)])
    visited[N - 1][M - 1] = True

    while q:
        x, y, cnt = q.popleft()

        if x == 0 and y == 0:
            return cnt

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny]: continue

            if maze[nx][ny] == '1':
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
            else:
                visited[nx][ny] = True
                q.appendleft((nx, ny, cnt))

    return -1

print(bfs())