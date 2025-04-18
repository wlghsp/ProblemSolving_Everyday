import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < M and 0 <= ny < N): continue
        if heights[x][y] <= heights[nx][ny]: continue

        dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))

