a = input()
b = input()
N = len(a)
M = len(b)
dp = [[-1] * (N + 1) for _ in range(M + 1)]

def dfs(i, j):
    if i == 0 or j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    if a[i - 1] == b[j - 1]:
        dp[i][j] = dfs(i - 1, j - 1) + 1
    else:
        dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))

    return dp[i][j]


print(dfs(N, M))
