N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * 10001
dp[0] = 1

for coin in coins:
    for amount in range(coin, K + 1):
        dp[amount] += dp[amount - coin]
print(dp[K])
