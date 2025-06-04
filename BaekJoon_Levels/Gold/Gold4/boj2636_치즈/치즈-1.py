import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
total = 0
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    total += sum(row)

def bfs():
    melts = []
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            if board[nx][ny] == 1:
                melts.append((nx, ny))
            else:
                q.append((nx, ny))

    for x, y in melts:
        board[x][y] = 0
    return len(melts)


time = 1

while True:
    cnt = bfs()
    total -= cnt
    if total == 0:
        print(time, cnt, sep='\n')
        break
    time += 1