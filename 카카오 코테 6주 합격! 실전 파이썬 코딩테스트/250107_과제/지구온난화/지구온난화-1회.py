

R, C = map(int, input().split())
dadohae = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_r, min_c, max_r, max_c = R, C, 0, 0

for x in range(R):
    for y in range(C):
        if dadohae[x][y] == 'X':
            count = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if dadohae[nx][ny] == '.':
                        count += 1
                else:
                    count += 1


            if count >= 3:
                dadohae[x][y] = 'S'


        if dadohae[x][y] == 'X':
            min_r = min(min_r, x)
            min_c = min(min_c, y)
            max_r = max(max_r, x)
            max_c = max(max_c, y)

for x in range(min_r, max_r + 1):
    for y in range(min_c, max_c + 1):
        if dadohae[x][y] == 'X':
            print(dadohae[x][y], end='')
        else:
            print('.', end='')
    print()