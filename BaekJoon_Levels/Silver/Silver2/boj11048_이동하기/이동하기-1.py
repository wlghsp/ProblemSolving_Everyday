import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0: continue

        if i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1] + maze[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j] + maze[i][j]
        elif i > 0 and j > 0:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i][j]
print(dp[N - 1][M - 1])
