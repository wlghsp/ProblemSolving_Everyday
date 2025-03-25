def find_heart(n, board):
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == '*' and board[i][j - 1] == '*' and board[i][j + 1] == '*'\
                    and board[i - 1][j] == '*' and board[i + 1][j] == '*':
                return i, j
    return -1, -1

N = int(input())
board = [input() for _ in range(N)]

hx, hy = find_heart(N, board)

# 왼쪽 팔, 오른쪽 팔
l_arm, r_arm = 0, 0
for i in range(hy + 1, N):
    if board[hx][i] == '*':
        r_arm += 1
    else:
        break
for i in range(hy - 1, -1, -1):
    if board[hx][i] == '*':
        l_arm += 1
    else:
        break
# 허리
waist = 0
for i in range(hx + 1, N):
    if board[i][hy] == '*':
        waist += 1
    else:
        break
#  왼쪽 다리, 오른쪽 다리
l_leg, r_leg = 0, 0
waist_end = hx + waist
for i in range(waist_end + 1, N):
    if board[i][hy - 1] == '*':
        l_leg += 1
    if board[i][hy + 1] == '*':
        r_leg += 1
print(hx + 1, hy + 1)
print(l_arm, r_arm, waist, l_leg, r_leg)
