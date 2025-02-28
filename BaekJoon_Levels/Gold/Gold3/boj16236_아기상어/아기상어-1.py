import heapq
from collections import deque

INF = 10 ** 9
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
cur_x, cur_y = 0, 0
fishes = deque()
for i in range(N):
    for j in range(N):
        if space[i][j] != 0:
            if space[i][j] == 9:
                cur_x, cur_y = i, j
            else:
                fishes.append((0, i, j))

time = 0
if len(fishes) == 0:
    print(0)
elif len(fishes) == 1:
    _, x, y = fishes.popleft()
    print((abs(cur_x - x) + abs(cur_y - y)))
else:
    baby_shark_size = 2

    # 거리 구하고 먹을 수 있는 물고기 찾기
    def bfs():
        dist = [[INF] * N for _ in range(N)]
        dist[cur_x][cur_y] = 0
        q = deque([(cur_x, cur_y)])

        while q:
            px, py = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = px + dx, py + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if dist[nx][ny] != INF: continue
                if baby_shark_size < space[nx][ny]: continue

                dist[nx][ny] = dist[px][py] + 1
                q.append((nx, ny))

        heap = []
        len_f = len(fishes)
        for i in range(len_f):
            _, x, y = fishes.popleft()
            heap.append((dist[x][y], x, y))

        heapq.heapify(heap)
        target_x, target_y = 0, 0
        min_dist = INF
        len_heap = len(heap)
        found = False
        for i in range(len_heap):
            d, x, y = heapq.heappop(heap)
            if space[x][y] < baby_shark_size and min_dist > d:
                min_dist, target_x, target_y = d, x, y
                found = True
            fishes.append((d, x, y))

        len_fishes = len(fishes)
        for i in range(len_fishes):
            d, x, y = fishes.popleft()
            if d == min_dist and target_x == x and target_y == y: continue
            fishes.append((d, x, y))

        return min_dist if found else -1, target_x, target_y


    ate_cnt = 0
    space[cur_x][cur_y] = 0
    while True:
        if len(fishes) == 0:
            break
        dist, cur_x, cur_y = bfs()
        if dist == -1:
            break
        space[cur_x][cur_y] = 0
        ate_cnt += 1
        time += dist

        if ate_cnt == baby_shark_size:
            baby_shark_size += 1
            ate_cnt = 0

    print(time)
