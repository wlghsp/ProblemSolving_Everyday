r, c = map(int, input().split())

dadohae = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_r, max_r, min_c, max_c = r, 0, c, 0

for x in range(r):
    for y in range(c):
        if dadohae[x][y] == 'X':
            count = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < r and ny >= 0 and ny < c:
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


for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        if dadohae[i][j] == 'X':
            print(dadohae[i][j], end='')
        else:
            print('.', end='')
    print()