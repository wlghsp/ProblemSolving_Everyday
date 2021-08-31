"""
입
72
출
2
2
2
3
3

입
3
출
3

입
6
출
2
3

입
2
출
2

입
9991
출
97
103
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())


def factorization(x):
    d = 2
    while x != 1:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d += 1


if n <= 1:
    print("")
else:
    factorization(n)
