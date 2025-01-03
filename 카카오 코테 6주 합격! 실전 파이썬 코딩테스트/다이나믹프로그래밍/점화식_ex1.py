

# 1, 4, 7, 10, 13 ...
# 15번째 항 : 43

# 점화식을 반복하는 기계를 만든다
# N번째 항  = N - 1 번째 항 + 3

# 위의 수열의 규칙을 지키는 n번째 항의 값을 출력
def func(n):
    # 각 항을 저장하는 배열을 만듬
    # 배열: lookup table
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 3

    return dp[n]

print(func(15))