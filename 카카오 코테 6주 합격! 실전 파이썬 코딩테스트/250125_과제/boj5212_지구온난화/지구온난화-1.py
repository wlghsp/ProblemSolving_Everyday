R, C = map(int, input().split())
before_map = [list(input()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_r, min_c, max_r, max_c = R, C, 0, 0

for x in range(R):
    for y in range(C):
        if before_map[x][y] == 'X':
            cnt = 0

            for i in range(4):
                 nx, ny = x + dx[i], y + dy[i]
                 if nx < 0 or nx >= R or ny < 0 or ny >= C: # 지도에서 벗어나는 칸은 모두 바다
                     cnt += 1
                 elif 0 <= nx < R and 0 <= ny < C and before_map[nx][ny] == '.': # 지도 안의 바다인 경우
                     cnt += 1
            if cnt >= 3:
                before_map[x][y] = 'S' # 바다로 변할 곳이나 다른 땅에 영향이 가지 않게 'S' 로 표시

        if before_map[x][y] == 'X': # 땅인 곳의 좌표로 출력 영역 구하기
            min_r, min_c, max_r, max_c = min(min_r, x), min(min_c, y), max(max_r, x), max(max_c, y)

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        if before_map[i][j] == 'X': # 땅은 그대로 출력
            print(before_map[i][j], end='')
        else: # 기존 바다와 바다로 바뀌는 땅(S) 출력
            print('.', end='')
    print()