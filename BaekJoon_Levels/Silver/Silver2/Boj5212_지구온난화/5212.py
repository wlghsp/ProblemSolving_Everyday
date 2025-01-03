import copy
import sys

input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
input_land = [ list(input()) for _ in range(R)]

padding_row = ['.'] * (C + 2)
original_land  = [padding_row] + [['.'] + row + ['.'] for row in input_land] + [padding_row] # 상단 패딩

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

future_land = copy.deepcopy(original_land)

for x in range(1, R + 1):
    for y in range(1, C + 1):
        if original_land[x][y] == '.':
            continue

        cnt = 0

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if original_land[nx][ny] == '.':
                cnt += 1

        if cnt >= 3:
            future_land[x][y] = '.'

min_r, max_r, min_c, max_c = float('inf'), -float('inf'), float('inf'), -float('inf')

for x in range(1, R + 1):
    for y in range(1, C + 1):
        if future_land[x][y] == 'X':
            min_r, min_c, max_r, max_c = min(x, min_r), min(y, min_c), max(x, max_r), max(y, max_c)

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(future_land[i][j], end='')
    print()