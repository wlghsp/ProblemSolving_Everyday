import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * 3 for _ in range(n)] # -1 이면 아직 계산 안한 상태

# i번째 집을 color(0:빨강, 1:초록, 2:파랑)로 칠했을 때 최소 비용
def dfs(i, color):
    if i == 0:
        return cost[0][color]

    if dp[i][color] != -1:
        return dp[i][color]

        # 현재 집 color에 따라 이전 집 색상 다르게 선택
    if color == 0:  # 현재 빨강
        dp[i][color] = cost[i][color] + min(dfs(i - 1, 1), dfs(i - 1, 2))
    elif color == 1:  # 현재 초록
        dp[i][color] = cost[i][color] + min(dfs(i - 1, 0), dfs(i - 1, 2))
    elif color == 2:  # 현재 파랑
        dp[i][color] = cost[i][color] + min(dfs(i - 1, 0), dfs(i - 1, 1))

    return dp[i][color]
# 마지막 집을 빨강/초록/파랑
result = min(dfs(n - 1, 0), dfs(n - 1, 1), dfs(n - 1, 2))
print(result)