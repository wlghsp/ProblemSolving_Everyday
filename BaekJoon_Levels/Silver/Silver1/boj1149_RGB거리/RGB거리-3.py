import sys
sys.setrecursionlimit(10 ** 6)
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

    best = float('inf')
    for j in range(3):
        if j != color:
            best = min(best, dfs(i - 1, j))

    dp[i][color] = best + cost[i][color]
    return dp[i][color]

# 마지막 집을 빨강/초록/파랑
result = min(dfs(n - 1, 0), dfs(n - 1, 1), dfs(n - 1, 2))
print(result)