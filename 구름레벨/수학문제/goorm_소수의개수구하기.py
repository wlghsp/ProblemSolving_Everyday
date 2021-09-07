"""
30

10

300

62

"""

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

n = int(input())


def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


count = 0
for i in range(2, n + 1):
    if is_prime_num(i):
        count += 1

print(count)
