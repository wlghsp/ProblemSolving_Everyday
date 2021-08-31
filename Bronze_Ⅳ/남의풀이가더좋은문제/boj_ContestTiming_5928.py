"""
12 13 14

1563

"""
import sys

input = lambda: sys.stdin.readline().rstrip()


d, h, m = map(int, input().split())
result = 0

# 전부 분으로 환산하여 차를 구하는게 가장 빨리 풀 수 있고 간단함.
start = 11 * 24 * 60 + 11 * 60 + 11
end = d * 24 * 60 + h * 60 + m

result = end - start

if result < 0:
    print(-1)
else:
    print(result)


# result = 0

# startingMin = 60 * 11 + 11
# endingMin = 60 * h + m

# if d >= 12:
#     result = endingMin + (24 * 60 - startingMin) + 1440 * (d - 12)
# elif d == 11 and endingMin >= startingMin:
#     result = endingMin - startingMin
# else:
#     result = -1

# print(result)
