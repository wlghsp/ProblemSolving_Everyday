
N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
matrix[r][c] = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_valid_move(x, y):
    return 0 <= x < N and 0 <= y < M

def clean(x, y, direction):
    global cnt
    matrix[x][y] = -1

    for i in range(4):
        direction = (direction + 3) % 4
        nx, ny = x + dx[direction], y + dy[direction]
        if is_valid_move(nx, ny) and matrix[nx][ny] == 0:
            cnt += 1
            clean(nx, ny, direction)
            return

    back = (direction + 2) % 4
    nx, ny = x + dx[back], y + dy[back]
    if is_valid_move(nx, ny) and matrix[nx][ny] != 1:
        clean(nx, ny, direction)

clean(r, c, d)


print(cnt)
