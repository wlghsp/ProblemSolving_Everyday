board = [list(input())  for _ in range(10)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x, board):
    board[y][x] = '*'

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10: continue
        if board[ny][nx] == '*': continue

        dfs(ny, nx, board)

x, y = map(int, input().split())

if board[y][x] == '_':
    dfs(y, x, board)

for row in board:
    print(''.join(row))