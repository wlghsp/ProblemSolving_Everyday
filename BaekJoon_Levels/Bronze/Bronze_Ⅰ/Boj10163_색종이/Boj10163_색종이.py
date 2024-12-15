import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 색종이의 장수
coordi = [[0] * 1001 for _ in range(1001)]
increment = 1
for _ in range(N):
    row, col, area, height = map(int, input().split())
    for r in range(row, row+area):
        coordi[r][col:col+height] = [increment] * height
    increment += 1

for k in range(1, N+ 1):
    cnt = 0
    for c in coordi:
        cnt += c.count(k)
    print(cnt)