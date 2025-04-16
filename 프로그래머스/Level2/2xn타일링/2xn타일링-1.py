
def solution(n):
    if n <= 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]

print(solution(4)) # 5

