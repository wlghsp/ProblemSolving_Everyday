

N = int(input())

def sugar(n):
    dp = [float('inf')] * (n + 1)
    dp[3] = 1
    if n >= 5:
        dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    return -1 if dp[n] == float('inf') else dp[n]

print(sugar(N))