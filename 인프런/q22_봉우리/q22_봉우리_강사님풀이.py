
N = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


board = []
for i in range(N):
    board.append(list(map(int, input().split())))

answer = 0

for i in range(N):
    for j in range(N):
        flag = True
        # 네 방향 확인
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0<= ny < N and board[nx][ny] >= board[i][j]:
                flag = False
                break

        if flag: answer += 1

print(answer)

