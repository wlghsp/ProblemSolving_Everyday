from collections import deque

N, M = map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(N)]
distance = [[-1] * M for _ in range(N)] # 도달할 수 없는 위치 -1 기록 위한 -1 초기화

target_x, target_y = -1, -1
for i in range(N):
    for j in range(M):
        if num_map[i][j] == 2:  # 목표 지점 찾은 경우
            target_x, target_y = i, j # 목표 지점 기록
        elif num_map[i][j] == 0: # 갈 수 없는 땅은 0으로 기록
            distance[i][j] = 0

# 목표 지점에서 시작하며 거리 초기화
q = deque([(target_x, target_y)])
distance[target_x][target_y] = 0

while q:
    x, y = q.popleft()

    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + i, y + j
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if distance[nx][ny] != -1: continue # -1 이 아니면 방문하지 않음
        if num_map[nx][ny] == 0: continue

        distance[nx][ny] = distance[x][y] + 1
        q.append((nx, ny))

for row in distance:
    print(*row)
