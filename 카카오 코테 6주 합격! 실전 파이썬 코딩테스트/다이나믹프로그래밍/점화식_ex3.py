

def func(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]

print(func(10))

# 문제를 읽고 DP 문제임을 발견한다.
# 문제를 이해해서 점화식을 찾는다
# 점화식을 위와 같이 프로그래밍 한다.
