"""
5

10.825317547305485

10

43.30127018922194

100000

4.330127018922194E9


"""
import sys

input = lambda: sys.stdin.readline().rstrip()

# 정육각형 한 변의 길이 L
l = int(input())
print((3 ** (0.5)) * (l ** 2) / 4)
