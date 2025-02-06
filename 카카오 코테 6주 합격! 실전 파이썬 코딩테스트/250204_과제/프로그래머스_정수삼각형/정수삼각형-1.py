def solution(t):
    dp = []
    for i in range(1, len(t) + 1):
        dp.append([0] * i)

    for i in range(len(t)):
        for j in range(len(t[i])):
            if j - 1 >= 0 and j + 1 < len(t[i]):
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + t[i][j]
            elif j - 1 < 0:
                dp[i][j] = dp[i - 1][j] + t[i][j]
            elif j + 1 >= len(t[i]):
                dp[i][j] = dp[i - 1][j - 1] + t[i][j]

    return max(max(row) for row in dp)


# 30
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t[i][j] (j - 1>= 0 and j + 1 < len(t[i]))

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))