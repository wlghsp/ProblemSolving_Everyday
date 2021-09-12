import math


def isSquare(num):
    return int(num ** 0.5) ** 2 == num


def solution(n):
    return int(((n ** 0.5) + 1) ** 2) if isSquare(n) else -1


n = 3
# print(isPowernum(n))
print(solution(n))
