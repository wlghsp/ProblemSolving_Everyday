

drawing_board = [list(input()) for _ in range(10)]
x, y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(y, x):
    if drawing_board[y][x] == '*':
        return

    drawing_board[y][x] = '*'

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10: continue
        if drawing_board[ny][nx] == '*': continue

        dfs(ny, nx)
def draw_board():
    for row in drawing_board:
        print(''.join(row))

dfs(y, x)

draw_board()


