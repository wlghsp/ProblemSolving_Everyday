"""
10110111

110000100111

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input(), 2)

n = n * 17

# 접두어 제외 2진수 변환 출력 format(10진수 숫자, 'b')
print(format(n, "b"))
