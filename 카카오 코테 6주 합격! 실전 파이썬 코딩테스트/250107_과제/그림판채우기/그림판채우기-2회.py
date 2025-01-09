

board = [list(input()) for _ in range(10)]
x, y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(y, x):
    board[y][x] = '*'

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= 10 or nx < 0 or nx >= 10: continue
        if board[ny][nx] == '*': continue

        dfs(ny, nx)



if board[y][x] == '_':
    dfs(y, x)


for row in board:
    print(''.join(row))