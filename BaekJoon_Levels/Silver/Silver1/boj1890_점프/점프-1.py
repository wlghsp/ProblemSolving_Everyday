import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def count_paths(x1, y1, x2, y2):
    dp = [[0] * (y2 - y1 + 1) for _ in range(x2 - x1 + 1)]
    dp[0][0] = 1

    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            if i == N - 1 and j == N - 1: continue # 도착점은 패스

            jump = board[i][j]
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]
            if j + jump < N:
                dp[i][j + jump] += dp[i][j]
    return dp[x2 - x1][y2 - y1]

print(count_paths(0, 0, N - 1, N - 1))