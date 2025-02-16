N, M, K = map(int, input().split())

def count_paths(x1, y1, x2, y2):
    dp = [[0] * (y2 - y1 + 1) for _ in range(x2 - x1 + 1)]
    dp[0][0] = 1

    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            if i == 0 and j == 0: continue

            from_top = dp[i - 1][j] if i > 0 else 0
            from_left = dp[i][j - 1] if j > 0 else 0
            dp[i][j] = from_top + from_left

    return dp[x2 - x1][y2 - y1]

if K == 0:
    print(count_paths(0, 0, N - 1, M - 1))
else:
    kx = (K - 1) // M
    ky = (K - 1) % M

    first_half = count_paths(0, 0, kx, ky)
    second_half = count_paths(kx, ky, N - 1, M - 1)
    print(first_half * second_half)