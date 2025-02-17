T = int(input())
max_n = 11
dp = [-1] * (max_n + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
def dfs(x):
    if dp[x] != -1:
        return dp[x]

    dp[x] = dfs(x - 1) + dfs(x - 2) + dfs(x - 3)
    return dp[x]

dfs(max_n)

for _ in range(T):
    num = int(input())
    print(dp[num])