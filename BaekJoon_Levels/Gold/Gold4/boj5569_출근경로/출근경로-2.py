import sys

sys.setrecursionlimit(10 ** 6)
W, H = map(int, input().split())

# k가 0=교차로 턴, 1= 연속, 2= 시작
dp = [[[[-1 for _ in range(3)] for _ in range(3)] for _ in range(H)] for _ in range(W)]
# 동쪽, 북쪽
dir = [(1, 0), (0, 1)]
MOD = 100000

def dfs(x, y, d, k):
    if x == W - 1 and y == H - 1:
        return 1

    if dp[x][y][d][k] != -1:
        return dp[x][y][d][k]

    dp[x][y][d][k] = 0

    for i in range(2):
        nx, ny = x + dir[i][0], y + dir[i][1]
        if not (0 <= nx < W and 0 <= ny < H): continue

        if k == 2:
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 1)) % MOD
        elif d == i: # 그전과 방향
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 1)) % MOD
        elif k == 1: # 방향이 다른데, 연속 상태이므로 방향 전환 가능
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 0)) % MOD


    return dp[x][y][d][k]


print(dfs(0, 0, 2, 2))