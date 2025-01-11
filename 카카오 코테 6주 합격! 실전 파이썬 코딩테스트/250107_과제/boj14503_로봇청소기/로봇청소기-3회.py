N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
matrix[r][c] = -1
dx = [-1, 0, 1, 0]
dy = [0, 1,  0, -1]

while True:
    cleaned = False

    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            cnt += 1
            matrix[nx][ny] = -1
            r, c = nx, ny
            cleaned = True
            break

    if not cleaned:
        rear = (d + 2) % 4
        nx, ny = r + dx[rear], c + dy[rear]
        # 후진이 불가능하면 종료
        if not (0 <= nx < N and 0 <= ny < M) or matrix[nx][ny] == 1:
            break

        # 후진이 가능하면 위치만 이동
        r, c = nx, ny

print(cnt)