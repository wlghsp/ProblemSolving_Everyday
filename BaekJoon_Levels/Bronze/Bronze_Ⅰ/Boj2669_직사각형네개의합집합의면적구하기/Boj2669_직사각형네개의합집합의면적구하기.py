import sys
input = lambda : sys.stdin.readline().rstrip()

coordi = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            coordi[i][j] += 1

width = 0
for a in range(len(coordi)):
    for b in range(len(coordi)):
        if coordi[a][b] > 0:
            width += 1
print(width)