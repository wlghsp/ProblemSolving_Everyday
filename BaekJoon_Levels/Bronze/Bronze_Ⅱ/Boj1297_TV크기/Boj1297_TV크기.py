
import sys

input = lambda: sys.stdin.readline().rstrip()

d, h, w = map(int, input().split())

# 대각선 길이 비를 구하고 그 비율로 곱해줘서 각 높이, 너비의 비율을 구한다.
r = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(h * r), int(w * r))
