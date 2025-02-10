a = input()
b = input()
len_a, len_b = len(a), len(b)
dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] != b[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = dp[i - 1][j - 1] + 1

r, c = len_a, len_b
result = [] # 문자열 + 보다 배열로 담는 것이 빠름
while dp[r][c] != 0:
    cur = dp[r][c]
    # 해당 좌표로 이동함
    if dp[r - 1][c] == cur:
        r -= 1 # r - 1, c 로 이동
    elif dp[r][c - 1] == cur:
        c -= 1 # r, c - 1 로 이동
    else: # 현재 값과 같지 않은 경우 = 문자가 같아서 +1 이 되었다는 의미
        # 해당 문자를 넣어 주고 r - 1, c - 1 로 이동
        result.append(a[r - 1])
        r -= 1
        c -= 1

print(dp[len_a][len_b])
print(''.join(result[::-1])) # 거꾸로 문자를 찾아가므로 출력할 때 역순 출력
