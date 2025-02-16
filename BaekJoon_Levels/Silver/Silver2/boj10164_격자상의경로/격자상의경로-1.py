
"""
오른쪽, 아래로만 이동 가능

"""
N, M, K = map(int, input().split())
if K == 0:
    pass
else:
    board = [[0] * M for _ in range(N)]
    num = 1
    n1, m1 = 0, 0
    for i in range(N):
        for j in range(M):
            if num == K:
                n1, m1 = i, j
            board[i][j] = num
            num += 1
    dp1 = [[0] * (m1 + 1) for _ in range(n1 + 1)]
    dp2 = [[0] * M for _ in range(N)]

    def dfs(x, y, n, m, dp):

        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

            dp[nx][ny] = dp[x][y] + 1

            dfs(nx, ny, n, m, dp)

    dfs(0, 0, n1 + 1, m1 + 1, dp1)
    print(dp1)





