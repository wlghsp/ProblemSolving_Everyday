def solution(x, y, n):
    dp = [-1] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == -1:
            continue
        for next_num in (i + n, i * 2, i * 3):
            if next_num <= y:
                if dp[next_num] == -1: # 계산한 적이 없음
                    dp[next_num] = dp[i] + 1 # 단순히 그전 숫자의 횟수에서 + 1
                else: # 계산한 적이 있음
                    dp[next_num] = min(dp[next_num], dp[i] + 1) # 둘 중에 비교

    return dp[y]


print(solution(10, 40, 5))  # 2
print(solution(2, 5, 4))  # -1
