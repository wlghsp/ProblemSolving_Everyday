

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

min_cnt = float('inf')

def check_board_color(start_row, start_col, pattern_start):
    cnt = 0
    for i in range(8):
        for j in range(8):
            expected = pattern_start
            if (i + j) % 2 != 0:
                expected = 'B' if pattern_start == 'W' else 'W'
            if board[start_row + i][start_col + j] != expected:
                cnt += 1

    return cnt

for i in range(N - 7):
    for j in range(M - 7):
        b_start = check_board_color(i, j, 'B')
        w_start = check_board_color(i, j, 'W')

        min_cnt = min(min_cnt, b_start, w_start)

print(min_cnt)