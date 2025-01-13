
board = [list(input()) for _ in range(10)]
x, y = map(int, input().split())

dx = [0,0, 1, -1]
dy = [1,-1, 0, 0]

def draw(y, x):
    board[y][x] = '*'

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if is_invalid_move(nx, ny): continue
        if board[ny][nx] == '*': continue

        draw(ny, nx)


def is_invalid_move(x, y):
    return y < 0 or y >= 10 or x < 0 or x >= 10


if board[y][x] == '_':
    draw(y, x)

for row in board:
    print(''.join(row))