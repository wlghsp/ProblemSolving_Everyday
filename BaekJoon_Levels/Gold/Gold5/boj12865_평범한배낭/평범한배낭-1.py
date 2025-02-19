import sys

input = lambda : sys.stdin.readline().rstrip()
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def dfs(item_idx, left_weight):
    if item_idx == N:
        return 0

    if dp[item_idx][left_weight] != -1:
        return dp[item_idx][left_weight]

    # 1. 현재 물건 안 담음 -> 다음 물건으로
    choice1 = dfs(item_idx + 1, left_weight)

    # 2. 현재 물건 담음 (무게 초과 안될 때만)
    choice2 = 0
    if items[item_idx][0] <= left_weight:
        choice2 = items[item_idx][1] + dfs(item_idx + 1, left_weight - items[item_idx][0])
    dp[item_idx][left_weight] = max(choice1, choice2)
    return dp[item_idx][left_weight]


print(dfs(0, K))
