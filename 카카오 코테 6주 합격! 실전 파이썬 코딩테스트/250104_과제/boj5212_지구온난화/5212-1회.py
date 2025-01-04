import copy

R, C = map(int, input().split())
input_land = [list(input()) for _ in range(R)]

padding_row = ['.'] * (C + 2)

original_land = [padding_row]
for row in input_land:
    original_land.append(['.'] + row + ['.'])
original_land.append(padding_row)

copy_land = copy.deepcopy(original_land)

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for x in range(1, R + 1):
    for y in range(1, C + 1):
        if original_land[x][y] == '.':
            continue

        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if original_land[nx][ny] == '.':
                cnt += 1

        if cnt >= 3:
            copy_land[x][y] = '.'


min_r, min_c, max_r, max_c = float('inf'), float('inf'), -float('inf'), -float('inf')

for x in range(1, R + 1):
    for y in range(1, C + 1):
        if copy_land[x][y] == 'X':
            min_r, min_c, max_r, max_c = min(x, min_r), min(y, min_c), max(x, max_r), max(y, max_c)

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(copy_land[i][j], end='')
    print()