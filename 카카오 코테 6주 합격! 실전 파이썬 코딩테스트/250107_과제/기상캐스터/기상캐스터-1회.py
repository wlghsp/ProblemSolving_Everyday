
H, W = map(int, input().split())

sky = [list(input()) for _ in range(H)]

clouds = [[-1] * W for _ in range(H)]

def update_sky():

    for i in range(H):
        for j in range(W):
            if sky[i][j] == 'c':
                clouds[i][j] = 0
                col = j + 1
                while col < W:
                    if sky[i][col] == 'c':
                        break
                    clouds[i][col] = clouds[i][col - 1] + 1
                    col += 1

update_sky()

for i in range(H):
    for j in range(W):
        print(clouds[i][j], end=' ')
    print()


