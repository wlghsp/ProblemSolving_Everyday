"""
4
1 3 5 7

3


"""

import math
import sys

input = lambda: sys.stdin.readline().rstrip()


def isPrimenum(n):
    """소수를 판별하는 함수"""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))

count = 0

for i in nums:
    if i <= 1:
        continue
    if isPrimenum(i):
        count += 1

print(count)
