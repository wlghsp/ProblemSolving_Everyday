def solution(m, n, puddles):
    dp = [[-1] * m for _ in range(n)]
    impossible = [[False] * m for _ in range(n)]
    for y, x in puddles:
        impossible[x - 1][y - 1] = True
    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return 1
        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0

        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m): continue
            if impossible[nx][ny]: continue

            dp[x][y] = (dp[x][y] + dfs(nx, ny)) % 1000000007
        return dp[x][y]


    return dfs(0, 0)

print(solution(4, 3, [[2, 2]])) # 4
