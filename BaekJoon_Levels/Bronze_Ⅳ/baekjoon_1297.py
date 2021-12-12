import sys

input = sys.stdin.readline

d, h, w = map(int, input().split())

k = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(k * h), int(k * w))
