
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def get_repaint_cnt(x, y, start):
    repaint_cnt = 0
    for i in range(8):
        for j in range(8):
            expected = start
            if (i + j) % 2 != 0:
                expected = 'W' if start == 'B' else 'B'
            if board[x + i][y + j] != expected:
                repaint_cnt += 1
    return repaint_cnt


min_cnt = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        b_start = get_repaint_cnt(i, j, 'B')
        w_start = get_repaint_cnt(i, j, 'W')

        min_cnt = min(min_cnt, b_start, w_start)

print(min_cnt)