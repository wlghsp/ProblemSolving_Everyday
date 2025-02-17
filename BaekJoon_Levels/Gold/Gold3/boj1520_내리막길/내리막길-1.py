import sys
sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]
dp =  [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1 # 도달하면 경우의 수 1 증가

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        if heights[x][y] <= heights[nx][ny]: continue

        dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))