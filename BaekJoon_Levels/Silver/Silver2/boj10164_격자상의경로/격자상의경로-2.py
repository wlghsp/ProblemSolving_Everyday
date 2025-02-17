N, M, K = map(int, input().split())

def dfs(x, y, n, m, dp):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in [(1, 0), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

        dp[x][y] += dfs(nx, ny, n, m, dp)
    return dp[x][y]

if K == 0:
    dp = [[-1] * M for _ in range(N)]
    print(dfs(0, 0, N, M, dp))
else:
    kx = (K - 1) // M
    ky = (K - 1) % M

    dp1 = [[-1] * (ky + 1) for _ in range(kx + 1)]
    dp2 = [[-1] * (M - ky) for _ in range(N - kx)]
    first_half = dfs(0, 0, kx + 1, ky + 1, dp1)
    second_half = dfs(0, 0, N - kx, M - ky, dp2)
    print(first_half * second_half)