
H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
cloud_time = [[-1] * W for _ in range(H)]

for x in range(H):
    for y in range(W):
        if sky[x][y] == 'c':
            cloud_time[x][y] = 0
            col = y + 1
            while col < W:
                if sky[x][col] == 'c':
                    break
                cloud_time[x][col] = cloud_time[x][col - 1] + 1
                col += 1

for i in range(H):
    for j in range(W):
        print(cloud_time[i][j], end=' ')
    print()
