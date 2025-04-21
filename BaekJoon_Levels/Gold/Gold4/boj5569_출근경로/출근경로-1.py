import sys

sys.setrecursionlimit(10 ** 6)
W, H = map(int, input().split())
dir = [(1, 0), (0, 1)]
# k = 0 최근에 바꿈, 1= 연속 방향, 2 = 시작 전
dp = [[[[-1 for _ in range(3)] for _ in range(3)] for _ in range(H)] for _ in range(W)]
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

        if k == 2: # 첫 시작
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 1)) % MOD
        elif d == i: # 방향 그대로
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 1)) % MOD
        elif k == 1: # 방향이 다르고 연속 이동 후
            dp[x][y][d][k] = (dp[x][y][d][k] + dfs(nx, ny, i, 0)) % MOD

    return dp[x][y][d][k]


print(dfs(0, 0, 2, 2))
