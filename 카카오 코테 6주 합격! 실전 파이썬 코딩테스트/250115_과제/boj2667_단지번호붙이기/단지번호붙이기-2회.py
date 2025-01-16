

N = int(input())
apartment = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

def dfs(x, y):
    apartment[x][y] = '0'
    cnt = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if apartment[nx][ny] == '0': continue

        cnt += dfs(nx, ny)
    return cnt

for i in range(N):
    for j in range(N):
        if apartment[i][j] == '1':
            cnt = dfs(i, j)
            result.append(cnt)



print(len(result))
for i in sorted(result):
    print(i)