def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    N = len(land)
    dp[0] = land[0][:]
    for row in range(1, N):
        for col in range(4):
            dp[row][col] = max(dp[row - 1][other] for other in range(4) if other != col) + land[row][col]
    return max(dp[N - 1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16