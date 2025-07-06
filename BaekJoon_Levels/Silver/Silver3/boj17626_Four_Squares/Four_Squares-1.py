import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [float('inf')] * 50001
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i - j * j] + 1, dp[i])

print(dp[n])