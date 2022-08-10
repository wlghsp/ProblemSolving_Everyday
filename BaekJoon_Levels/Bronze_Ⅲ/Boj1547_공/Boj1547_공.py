import sys
input = lambda : sys.stdin.readline().rstrip()

position = [0, 1, 2, 3]
M = int(input()) # 컵의 위치를 바꾼 횟수
for _ in range(M):
    x, y = map(int, input().split())
    xloc = position.index(x)
    yloc = position.index(y)
    position[xloc] = y
    position[yloc] = x


print(position[1])
