"""
60
100

620
61

64
65

-1

"""
import sys
import math

input = lambda: sys.stdin.readline().rstrip()


def isPrimenum(k):
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return False
    return True


m = int(input())
n = int(input())

primenums = []
for i in range(m, n + 1):
    if i <= 1:
        continue
    if isPrimenum(i):
        primenums.append(i)

if primenums:
    print(sum(primenums))
    print(min(primenums))
else:
    print(-1)
