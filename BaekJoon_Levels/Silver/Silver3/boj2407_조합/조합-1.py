dp = [[-1] * 101 for _ in range(101)]

def dfs(n, m):
    if dp[n][m] != -1:
        return dp[n][m]
    if n == m or m == 0:
        return 1

    dp[n][m] = dfs(n - 1, m) + dfs(n - 1, m - 1)
    return dp[n][m]

n, m = map(int, input().split())
print(dfs(n, m))