
import sys
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
castle = []
for i in range(N):
    castle.append(input())
row = 0
for i in range(N):
   if 'X' not in castle[i]:
       row += 1

col = 0
for j in range(M):
    if "X" not in [castle[i][j] for i in range(N)]:
        col += 1

print(max(row, col))