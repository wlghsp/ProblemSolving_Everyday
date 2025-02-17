import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]

def three_point_check(x, y):
    for dx, dy in [(0, 1), (1, 0), (1, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N: return False
        if house[nx][ny] == 1: return False
    return True

def can_move(x, y):
    return x < N and y < N and house[x][y] == 0

def move_diagonal(direction, x, y):
    if three_point_check(x, y):  # 대각선
        dp[x][y][direction] += dfs(x + 1, y + 1, 2)

def move_down(direction, x, y):
    if can_move(x + 1, y):  # 아래
        dp[x][y][direction] += dfs(x + 1, y, 1)

def move_right(direction, x, y):
    if can_move(x, y + 1):  # 오른쪽
        dp[x][y][direction] += dfs(x, y + 1, 0)

def dfs(x, y, direction):
    if x == N - 1 and y == N - 1:
        return 1

    if dp[x][y][direction] != -1:
        return dp[x][y][direction]

    dp[x][y][direction] = 0

    if direction == 0:
        move_right(direction, x, y)
    elif direction == 1:
        move_down(direction, x, y)
    elif direction == 2:
        move_right(direction, x, y)
        move_down(direction, x, y)

    move_diagonal(direction, x, y)
    return dp[x][y][direction]

print(dfs(0, 1, 0))
