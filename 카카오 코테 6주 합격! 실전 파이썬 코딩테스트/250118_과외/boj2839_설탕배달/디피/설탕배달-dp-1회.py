
N = int(input())

MAX_NUM = 5000

dp = [float('inf')] * (MAX_NUM + 1)

if N <= 2:
    print(0)

dp[3] = 1
dp[5] = 1

for i in range(6, N + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(-1 if dp[N] == float('inf') else dp[N])