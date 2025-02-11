a = input()
b = input()
len_a, len_b = len(a), len(b)
dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

r, c = len_a, len_b
result = []
while dp[r][c] != 0:
    if dp[r][c] == dp[r - 1][c]:
        r -= 1
    elif dp[r][c] == dp[r][c - 1]:
        c -= 1
    else:
        result.append(a[r - 1])
        r -= 1
        c -= 1

print(dp[len_a][len_b])
print(''.join(result[::-1]))