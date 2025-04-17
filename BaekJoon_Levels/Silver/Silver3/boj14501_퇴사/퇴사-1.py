import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    t, p = meetings[i]
    if i + t <= N:
        dp[i] = max(p + dp[i + t], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])