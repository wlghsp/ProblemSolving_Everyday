def dfs(house, color):
    if house == 0:
        return costs[0][color]

    if dp[house][color] != -1:
        return dp[house][color]

    min_cost = float('inf')
    for prev_color in range(3):
        if prev_color != color:
            min_cost = min(min_cost, dfs(house - 1, prev_color))

    dp[house][color] = min_cost + costs[house][color]
    return dp[house][color]

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * 3 for _ in range(N)]
result = min(dfs(N - 1, 0), dfs(N - 1, 1), dfs(N - 1, 2))
print(result)