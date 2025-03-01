import heapq
from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
cur_x, cur_y = 0, 0
# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            cur_x, cur_y = i, j
            space[i][j] = 0

time = 0
baby_shark_size = 2
ate_cnt = 0

# 거리 구하고 먹을 수 있는 물고기 찾기
def bfs():
    dist = [[-1] * N for _ in range(N)]
    dist[cur_x][cur_y] = 0
    q = deque([(cur_x, cur_y)])

    heap = []
    while q:
        px, py = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = px + dx, py + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if dist[nx][ny] != -1: continue
            if baby_shark_size < space[nx][ny]: continue

            dist[nx][ny] = dist[px][py] + 1
            q.append((nx, ny))

            # 먹을 수 있는 물고기만 힙에 넣음
            if 0 < space[nx][ny] < baby_shark_size:
                heapq.heappush(heap, (dist[nx][ny], nx, ny))

    return heap[0] if heap else (-1, -1, -1)

# 아기 상어 이동 & 물고기 먹기
while True:
    dist, nx, ny = bfs()
    if dist == -1:
        break

    # 이동 및 시간 증가
    cur_x, cur_y = nx, ny
    space[cur_x][cur_y] = 0
    ate_cnt += 1
    time += dist

    if ate_cnt == baby_shark_size:
        baby_shark_size += 1
        ate_cnt = 0

print(time)
