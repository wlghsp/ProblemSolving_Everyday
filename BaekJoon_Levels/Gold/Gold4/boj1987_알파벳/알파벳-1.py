import sys

input = lambda : sys.stdin.readline().rstrip()
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
max_cnt = 0

def dfs(x, y, visited, count):
    global max_cnt
    max_cnt = max(max_cnt, count)

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < R and 0 <= ny < C): continue
        if visited & (1 << ord(board[nx][ny]) - ord('A')): continue

        dfs(nx, ny, visited | (1 << (ord(board[nx][ny]) - ord('A'))), count + 1)

bitmask = 0
dfs(0, 0, bitmask | (1 << (ord(board[0][0]) - ord('A'))), 1)

print(max_cnt)
