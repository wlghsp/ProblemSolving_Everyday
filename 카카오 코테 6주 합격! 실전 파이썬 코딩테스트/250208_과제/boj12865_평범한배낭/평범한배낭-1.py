''''
3 10
5 5
3 4
4 5

  0 1 2 3 4 5 6 7 8 9 10
0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 5 5 5 5 5 5
2 0 0 0 4 4 5 5 5 9 9 9
3 0 0 0 4 5 5 5 9 9 10 10

'''

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(1, K + 1):
        dp[i][w] = dp[i - 1][w]
        if w - weight >= 0:
            dp[i][w] = max(dp[i - 1][w - weight] + value, dp[i - 1][w])
print(dp[N][K])