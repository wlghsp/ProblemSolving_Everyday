
N = int(input())
apart = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

answer = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if apart[nx][ny] == '0': continue
        if visited[nx][ny]: continue

        cnt += dfs(nx, ny)
    return cnt

for i in range(N):
    for j in range(N):
        if not visited[i][j] and apart[i][j] == '1':
            cnt = dfs(i, j)
            answer.append(cnt)


print(len(answer))
for i in sorted(answer):
    print(i)