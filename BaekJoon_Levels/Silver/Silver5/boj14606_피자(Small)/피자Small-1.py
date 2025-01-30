N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    half_i = i // 2
    dp[i] = half_i * (i - half_i) + dp[half_i] + dp[i - half_i]

def dp(n):
    if n == 1:
        return 0
    half_n = n // 2

    return half_n * (n - half_n) + dp(half_n) + dp(n - half_n)

print(dp(N))
