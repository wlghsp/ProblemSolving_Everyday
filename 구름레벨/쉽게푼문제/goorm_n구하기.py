"""
1000
45

200
20

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

result = 0
sumofnum = 0
for i in range(1, n + 1):
    sumofnum += i
    if sumofnum > n:
        result = i
        break

print(result)
