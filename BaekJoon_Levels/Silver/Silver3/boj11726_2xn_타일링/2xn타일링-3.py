def solve(N):
    dp = [0] * (N + 1)

    if N <= 3:
        return N
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[N]

n = int(input())
print(solve(n))