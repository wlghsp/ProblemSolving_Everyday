"""
N x N 크기의 공간에 물고기 M마리와 아기상어 1마리
한 칸에는 물고기가 최대 1마리 존재

fisrt baby_shark_size = 2
1초에 상하좌우 이동

- if baby_shark_size < fish_size: continue
- baby_shark_size >=  fish_size:
    if baby_shark_size > fish_size:
        baby_shark can eat
-   else:
        baby_shark just can pass by
1. 더 이상 먹을 물고기 없으면 종료
2. 1마리라면 그 물고기 먹으러 간다
3. 1마리 초과라면 가장 가까운 물고기를 먹으러 감
    - 거리는 지나야하는 칸의 개수의 최솟값
    - 거리가 같다면, x asc, y asc
아기상어 크기와 같은 수의 물고기 먹으면 크기 증가
if ate_cnt == baby_shark_size:
    baby_shark_size += 1
"""
import sys
from collections import deque

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
                fishes.append((i, j))

time = 0
if len(fishes) == 0:
    print(time)
else:
    baby_shark_size = 2
    # 거리 구하기
    def bfs():
        dist = [[0] * N for _ in range(N)]
        q = deque([(cur_x, cur_y)])

        while q:
            px, py = q.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = px + dx, py + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if dist[nx][ny] != 0: continue
                if baby_shark_size < space[nx][ny]: continue

                dist[nx][ny] = dist[px][py] + 1
                q.append((nx, ny))
        min_dist = sys.maxsize
        min_x, min_y = 0, 0
        while fishes:
            if min_dist > dist[nx][ny]:
                min_dist = dist[nx][ny]
                min_x, min_y = nx, ny
        return min_x, min_y

    ate_cnt = 0
    while fishes:
        if len(fishes) == 1:
            cur_x, cur_y = fishes[0], fishes[1]
        elif len(fishes) > 1:
            cur_x, cur_y = bfs()


        if ate_cnt == baby_shark_size:
            baby_shark_size += 1


    print(time)
