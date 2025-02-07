import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]
dp = []
for i in range(1, N + 1):
    dp.append([0] * i)

dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[N - 1]))