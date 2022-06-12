import sys
input = lambda : sys.stdin.readline().rstrip()

coordi = [[0] * 100 for _ in range(100)] # 좌표평면

N = int(input()) # 색종이의 수

# 색종이를 붙인 위치
# Boj2669_직사각형네개의합집합의면적구하기 와 같은 문제

for _ in range(N):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 10, y1 + 10

    for i in range(x1, x2):
        for j in range(y1, y2):
            coordi[i][j] = 1

answer = 0
for a in range(len(coordi)):
    for b in range(len(coordi)):
        if coordi[a][b] > 0:
            answer += 1

print(answer)
