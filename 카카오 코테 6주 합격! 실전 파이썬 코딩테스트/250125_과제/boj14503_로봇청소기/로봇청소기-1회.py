N, M = map(int, input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
matrix = [list(map(int, input().split())) for _ in range(N)]
clean_space_cnt = 1


def clean(x, y, direction):
    global clean_space_cnt
    matrix[x][y] = 2

    for i in range(4):
        direction = (direction + 3) % 4
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            clean_space_cnt += 1
            clean(nx, ny, direction)
            return

    back = (direction + 2) % 4
    nx, ny = x + dx[back], y + dy[back]
    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != 1:
            clean(nx, ny, direction)

clean(r, c, d)
print(clean_space_cnt)