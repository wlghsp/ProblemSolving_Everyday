
# 초기항의 값 = 1
# 5번째 항의 값
# 답: 144801

# An + 1 = 19 * An + 2

def func(n):

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = 19 * dp[i - 1] + 2
    return dp[n]

print(func(5))