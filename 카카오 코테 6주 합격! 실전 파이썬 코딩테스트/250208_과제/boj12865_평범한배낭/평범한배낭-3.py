import sys

input = sys.stdin.readline
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(1, K + 1):
        if w >= weight:
            # 현재 아이템을 배낭에 넣는 경우와 배낭에 넣지 않는 경우의 가치를 비교
            dp[i][w] = max(dp[i - 1][w - weight] + value, dp[i - 1][w])
        else:
            # 현재 아이템을 넣을 수 없으므로 넣지 않는 경우의 가치를 그대로 할당
            dp[i][w] = dp[i - 1][w]
print(dp[N][K])