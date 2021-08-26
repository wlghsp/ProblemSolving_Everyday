"""
약수의 합

10

18

20

42

"""
import sys

input = sys.stdin.readline

n = int(input())
result = 1
for i in range(2, n + 1):
    if n % i == 0:
        result += i
print(result)
