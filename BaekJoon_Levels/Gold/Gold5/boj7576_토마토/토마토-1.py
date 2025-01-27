# M 가로 N 세로
# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 토마토가 없음
# 토마토가 모두 익는 최소 날짜 출력
# 처음부터 모두 익어 있는 상태이면 0 출력, 토마토가 모두 익지 못하는 상황이라면 -1 출력
from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
days = [[0] * M for _ in range(N)]


def is_all_riped():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True

# 모두 익은 상태이면 0 출력
if is_all_riped():
    print(0)
else:
    # 1.익은 토마토를 찾아 큐에 담는다.
    q = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i, j))

    def bfs():
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if days[nx][ny] != 0: continue
                if box[nx][ny] != 0: continue

                days[nx][ny] = days[x][y] + 1
                box[nx][ny] = 1
                q.append((nx, ny))

    # 2. 탐색하여 익은 토마토들에서 시작하여 안 익은 토마토 익히며 날짜 갱신
    bfs()

    # 3. 모두 익었는지 확인하고 가장 큰 날짜 찾고, 모두 안 익었다면 -1 출력
    last_day = -1
    all_riped = True
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                all_riped = False
            last_day = max(last_day, days[i][j])


    print(last_day if all_riped else -1)