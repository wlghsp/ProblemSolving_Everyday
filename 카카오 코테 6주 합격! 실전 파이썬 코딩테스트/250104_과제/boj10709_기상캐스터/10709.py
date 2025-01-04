# 1 + H 행
# 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동
# 구름이 있는 경우 'c' 구름이 없는 경우 '.'

# 입력
H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
result = [[-1] * W for _ in range(H)]

# sky를 탐색해서 result 에 기록
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c': # 구름 발견
            result[i][j] = 0
            cur_col = j + 1

            while cur_col < W:
                if sky[i][cur_col] == 'c':
                    break
                elif sky[i][cur_col] == '.':
                    result[i][cur_col] =  result[i][cur_col - 1] + 1

                cur_col += 1

# 출력
for i in range(H):
    for j in range(W):
        print(result[i][j], end=' ')
    print()
