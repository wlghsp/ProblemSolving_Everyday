from collections import deque

for _ in range(int(input())):
    N = int(input())
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

    def bfs():
        distance = [[-1] * N for _ in range(N)]

        q = deque()
        q.append((cx, cy))
        distance[cx][cy] = 0

        while q:
            x, y = q.popleft()
            if x == tx and y == ty:
                print(distance[x][y])
                return

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if distance[nx][ny] != -1: continue

                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    bfs()
