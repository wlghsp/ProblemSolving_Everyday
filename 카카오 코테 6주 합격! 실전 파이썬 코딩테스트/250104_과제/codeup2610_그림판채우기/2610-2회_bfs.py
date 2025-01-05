
from collections import deque

board = [list(input()) for _ in range(10)]
x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_y, start_x):
    board[start_y][start_x] = '*'
    dq = deque([(start_y, start_x)])

    while dq:
        cur_y, cur_x = dq.popleft()

        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if next_y < 0 or next_y >= 10 or next_x < 0 or next_x >= 10: continue
            if board[next_y][next_x] == '*': continue

            board[next_y][next_x] = '*'
            dq.append((next_y, next_x))


if board[y][x] == '_':
    bfs(y, x)

for row in board:
    print(''.join(row))
