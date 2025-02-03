import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

all_ripe = True

# 모두 익었는지 확인
for i in range(N):
    for j in range(M):
        if box[i][j] != 1:
            all_ripe = False
            break

if all_ripe: # 익은 상태면 0 출력
    print(0)
else:
    days = [[0] * M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1: # 익은 토마토
                q.append((i, j))

    while q:
        px, py = q.popleft()

        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = px + i, py + j
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if box[nx][ny] != 0: continue
            if days[nx][ny] != 0: continue

            days[nx][ny] = days[px][py] + 1
            box[nx][ny] = 1
            q.append((nx, ny))

    def cannot_all_ripe():
        for i in range(N):
            for j in range(M):
                if box[i][j] == 0: # 안 익은 토마토
                    return True
        return False

    print(-1 if cannot_all_ripe() else max(max(row) for row in days))