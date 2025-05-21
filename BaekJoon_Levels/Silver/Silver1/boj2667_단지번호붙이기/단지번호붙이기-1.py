import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
ans = []
town = []
for _ in range(N):
    town.append(list(input()))
visited = [[False] * N for _ in range(N)]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N): continue
        if visited[nx][ny]: continue
        if town[nx][ny] == '0': continue

        count += dfs(nx, ny)

    return count

for i in range(N):
    for j in range(N):
        if not visited[i][j] and town[i][j] == '1':
            res = dfs(i, j)
            ans.append(res)

ans.sort()

print(len(ans))
print(*ans, sep='\n')