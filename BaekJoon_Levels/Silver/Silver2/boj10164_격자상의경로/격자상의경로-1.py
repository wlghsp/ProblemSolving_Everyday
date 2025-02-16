N, M, K = map(int, input().split())

if K == 0:
    dp = [[0] * M for _ in range(N)]
    for i in range(N):  # 위에서 오는 경우
        dp[i][0] = 1
    for i in range(M):  # 왼쪽에서 오는 경우
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(1, M):
            # 위에서 내려 오거나, 왼쪽에서 오거나
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[N - 1][M - 1])
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
    for i in range(n1 + 1): # 위에서 오는 경우
        dp1[i][0] = 1
    for i in range(m1 + 1): # 왼쪽에서 오는 경우
        dp1[0][i] = 1
    for i in range(1, n1 + 1):
        for j in range(1, m1 + 1):
            # 위에서 내려 오거나, 왼쪽에서 오거나
            dp1[i][j] = dp1[i - 1][j] + dp1[i][j - 1]

    dp = [[0] * M for _ in range(N)]
    for i in range(n1, N):  # 위에서 오는 경우
        dp[i][m1] = 1
    for i in range(m1, M):  # 왼쪽에서 오는 경우
        dp[n1][i] = 1
    for i in range(n1 + 1, N):
        for j in range(m1 + 1, M):
            # 위에서 내려 오거나, 왼쪽에서 오거나
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp1[n1][m1] * dp[N - 1][M - 1])
