import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
distance = [[-1] * M for _ in range(N)]
box = []
queue = deque()
def pre_process():
    for i in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        for j in range(len(row)):
            if row[j] == 1:
                queue.append((i, j))
                distance[i][j] = 0

def is_all_riped():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True

pre_process()

if is_all_riped():
    print(0)
else:

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if distance[nx][ny] != -1: continue
            if box[nx][ny] != 0: continue

            distance[nx][ny] = distance[x][y] + 1
            box[nx][ny] = 1
            queue.append((nx, ny))

    print(max(max(row) for row in distance) if is_all_riped() else -1)
