
import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

board = [input() for _ in range(N)]

ans = N * M

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if board[y + i][x + j] == bw:
                    cnt += 1
            else:
                if board[y + i][x + j] != bw:
                    cnt += 1
    ans = min(ans, cnt)


for y in range(N - 7):
    for x in range(M - 7):
        fill(y, x, 'B')
        fill(y, x, 'W')

print(ans)