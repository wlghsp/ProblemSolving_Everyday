import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

if N == 1:
    print(stairs[1])
    exit()

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

if N == 2:
    print(dp[2])
    exit()

for i in range(3, N + 1):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[N])