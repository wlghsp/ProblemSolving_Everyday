H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
cloud_record = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            cloud_record[i][j] = 0
            col = j + 1
            while col < W:
                if sky[i][col] == 'c':
                    break
                cloud_record[i][col] = cloud_record[i][col - 1] + 1
                col += 1

for i in range(H):
    for j in range(W):
        print(cloud_record[i][j], end=' ')
    print()
