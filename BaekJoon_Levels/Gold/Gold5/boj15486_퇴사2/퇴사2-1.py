import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

dp = [-1] * (N + 1)

def dfs(n):
    if n >= N:
        return 0

    if dp[n] != -1:
        return dp[n]

    skip = dfs(n + 1)

    take = 0
    if n + meetings[n][0] <= N:
        take = meetings[n][1] + dfs(n + meetings[n][0])

    dp[n] = max(take, skip)
    return dp[n]

print(dfs(0))