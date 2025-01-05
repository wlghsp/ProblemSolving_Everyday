import copy

R, C = map(int, input().split())

input_map = [list(input()) for _ in range(R)]

padding_row = ['.'] * (C + 2)
original_map = [padding_row] + [['.'] + row + ['.'] for row in input_map] + [padding_row]
fifty_years_later_map = copy.deepcopy(original_map)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 복사 지도 변경
def update_copy_map():
    for x in range(1, R + 1):
        for y in range(1, C + 1):
            if original_map[x][y] == '.':
                continue

            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if original_map[nx][ny] == '.':
                    cnt += 1

            if cnt >= 3:
                fifty_years_later_map[x][y] = '.'

# 최소 최대 행열 구하기
def get_min_max_row_col():
    min_r, min_c, max_r, max_c = float('inf'), float('inf'), -float('inf'), -float('inf')

    for x in range(1, R + 1):
        for y in range(1, C + 1):
            if fifty_years_later_map[x][y] == 'X':
                min_r, min_c, max_r, max_c = min(x, min_r), min(y, min_c), max(x, max_r), max(y, max_c)

    return min_r, min_c, max_r, max_c

# 출력
def print_map(min_r, min_c, max_r, max_c):
    for i in range(min_r, max_r + 1):
        for j in range(min_c, max_c + 1):
            print(fifty_years_later_map[i][j], end='')
        print()

update_copy_map()
min_r, min_c, max_r, max_c = get_min_max_row_col()
print_map(min_r, min_c, max_r, max_c)