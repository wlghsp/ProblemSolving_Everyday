
N = int(input())

dp = [0] * 1001

def dfs(n):
    if n <= 2:
        return n
    if dp[n] != 0:
        return dp[n]

    dp[n] = (dfs(n - 1) + dfs(n - 2)) % 10007
    return dp[n]

print(dfs(N))