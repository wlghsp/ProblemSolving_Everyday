
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def get_repaint_cnt(x, y, start_color):
    cnt = 0

    for i in range(8):
        for j in range(8):
            expected = start_color
            if (i + j) % 2 != 0:
                expected = 'W' if start_color == 'B' else 'B'
            if board[x + i][y + j] != expected:
                cnt += 1

    return cnt


min_cnt = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        b_start_cnt = get_repaint_cnt(i, j, 'B')
        w_start_cnt = get_repaint_cnt(i, j, 'W')

        min_cnt  = min(min_cnt, b_start_cnt, w_start_cnt)

print(min_cnt)