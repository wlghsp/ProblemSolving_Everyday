import math
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = 1
grp = 1
while True:
    if result >= n:
        break
    result += 6 * grp
    grp += 1

print(grp)
