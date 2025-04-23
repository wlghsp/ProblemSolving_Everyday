import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(N):
    T[i], P[i] = map(int, input().split())
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])