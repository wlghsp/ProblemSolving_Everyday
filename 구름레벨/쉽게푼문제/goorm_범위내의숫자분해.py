"""
원제: 범위 내의 숫자를 분해하여 곱한 후 합 구하기 

10 20

45


10 100

2025

"""

import sys

input = lambda: sys.stdin.readline().rstrip()


start, end = map(int, input().split())

result = 0

for num in range(start, end + 1):
    num_str = list(str(num))
    multipleOfNum = 1
    for n in num_str:
        multipleOfNum *= int(n)
    result += multipleOfNum

print(result)
