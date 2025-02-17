import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

def dfs(x, y):
    if x == N - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx, dy in [(1, 0), (0, 1)]:
        nx, ny = x + (dx * board[x][y]), y + (dy * board[x][y])
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

        dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))