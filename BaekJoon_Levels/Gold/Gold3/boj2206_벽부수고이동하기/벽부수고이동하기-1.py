import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


def bfs():
    distance = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 0)])
    distance[0][0][0] = 1

    while q:
        x, y, broken = q.popleft()

        if x == N - 1 and y == M - 1:
            return distance[x][y][broken]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue

            if board[nx][ny] == '0' and distance[nx][ny][broken] == -1:
                distance[nx][ny][broken] = distance[x][y][broken] + 1
                q.append((nx, ny, broken))
            elif board[nx][ny] == '1' and broken == 0 and distance[nx][ny][1] == -1:
                distance[nx][ny][1] = distance[x][y][broken] + 1
                q.append((nx, ny, 1))
    return -1

print(bfs())
