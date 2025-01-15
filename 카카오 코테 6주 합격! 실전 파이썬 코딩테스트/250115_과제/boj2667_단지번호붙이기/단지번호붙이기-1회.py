N = int(input())
apart = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

def dfs(x, y):
    apart[x][y] = '0' # 방문 처리
    cnt = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if apart[nx][ny] == '0': continue

        cnt += dfs(nx, ny)
    return cnt

for i in range(N):
    for j in range(N):
        if apart[i][j] == '1':
            answer.append(dfs(i, j))

print(len(answer))
for i in sorted(answer):
    print(i)
