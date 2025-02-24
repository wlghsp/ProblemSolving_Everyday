import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
wines =  [0] * (10000 + 1)
for i in range(1, N + 1):
    wines[i] = int(input())

dp = [0] * (10000 + 1)
dp[1] = wines[1]
dp[2] = wines[1] + wines[2]
dp[3] = max(dp[2], wines[1] + wines[3], wines[2] + wines[3])
for i in range(4, 10000 + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], wines[i] + wines[i - 1] + dp[i - 3])
print(max(dp))