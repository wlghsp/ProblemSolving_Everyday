
R, C = map(int, input().split())
land = [list(input()) for _ in range(R)]

min_r, min_c, max_r, max_c = R, C, 0, 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(R):
    for y in range(C):
        if land[x][y] == 'X':

            cnt = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if land[nx][ny] == '.':
                        cnt += 1
                else:
                    cnt += 1

            if cnt >= 3:
                land[x][y] = 'S'

        if land[x][y] == 'X':
            min_r = min(min_r, x)
            min_c = min(min_c, y)
            max_r = max(max_r, x)
            max_c = max(max_c, y)


for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        if land[i][j] == 'X':
            print(land[i][j], end='')
        else:
            print('.', end='')
    print()