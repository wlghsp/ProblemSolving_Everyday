N = int(input())
dp = [0] * 16
dp[0] = 2
dp[1] = 3
dp[2] = 5
# 한변의 점의 갯수는 dp[i] = 2 * dp[i - 1] - 1
for i in range(3, 16):
    dp[i] = 2 * dp[i - 1] - 1

# 총 점의 갯수는 한변의 점의 갯수 제곱 = dp[N] * dp[N]
print(dp[N] * dp[N])