a = input()
b = input()
length_a, length_b = len(a), len(b)
dp = [[0] * (length_b + 1) for _ in range(length_a + 1)]

for i in range(1, length_a + 1):
    for j in range(1, length_b + 1):
        if a[i - 1] == b[j - 1]: # 문자가 같다면
            dp[i][j] = dp[i - 1][j - 1] + 1
        else: # 다른 경우
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(max(row) for row in dp))
