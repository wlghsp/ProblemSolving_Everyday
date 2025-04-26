import sys


input = lambda : sys.stdin.readline().rstrip()
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(K + 1): # 배낭의 남은 허용 무게 w 0 ~ K
        if w < weight: # 현재 물건을 배낭에 넣을 수 없는 경우
            dp[i][w] = dp[i - 1][w]
        else: # 현재 물건을 배낭에 넣을 수 있는 경우
            # 현재 물건을 넣거나, 안 넣는 경우
            # 1. dp[i - 1][w]: 이번 물건을 넣지 않았을 때 가치
            # 2. dp[i - 1][w - weight]: 이번 물건을 넣었을 때 가치
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[N][K])

