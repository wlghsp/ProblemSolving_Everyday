
N = int(input())

points = [0] + [int(input())  for _ in range(N)]

dp = [0] * (N + 1)

dp[1] = points[1]
if N > 1:
    dp[2] = points[1] + points[2]
if N > 2:
    dp[3] = max(points[1] + points[3], points[2] + points[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 2] + points[i], dp[i - 3] + points[i - 1] + points[i])

print(dp[N])
