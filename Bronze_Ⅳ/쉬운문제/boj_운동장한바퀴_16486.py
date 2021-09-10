"""
13
8

76.265472

영역C의 가로길이 d1
영역A의 반지름의 길이 d2

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

# 영역C의 가로길이 d1
d1 = int(input())
# 영역A의 반지름의 길이 d2
d2 = int(input())
pie = 3.141592
result = 2 * d1 + 2 * pie * d2

print(result)