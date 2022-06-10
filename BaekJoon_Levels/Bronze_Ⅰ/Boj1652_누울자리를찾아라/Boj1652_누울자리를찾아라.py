import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

room = [input() for _ in range(N)]

ans = [0, 0]
for i in range(N):
    row, col = 0, 0
    for j in range(N):
        # 가로
        if room[i][j] == '.':
            row += 1
        else:
            row = 0
        if row == 2:
            ans[0] += 1

        # 세로
        if room[j][i] == '.':
            col += 1
        else:
            col = 0
        if col == 2:
            ans[1] += 1

print(*ans)
