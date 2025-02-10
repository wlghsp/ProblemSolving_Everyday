import sys

input = sys.stdin.readline
N = int(input())
costs = [[0, 0, 0]]
costs += [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = min(dp[i-1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i - 1][0]) + costs[i][2]

print(min(dp[N][0], dp[N][1], dp[N][2]))
