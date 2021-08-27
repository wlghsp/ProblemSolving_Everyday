"""
5
1
35
25
55
44

2

3
81
1
49

3
"""


import sys

input = lambda: sys.stdin.readline().rstrip()

# 제곱수 판별
# 제곱을 풀고 정수로 만들어 제곱을 다시 했을 때 원래 수와 같은지로 확인
def isSquare(n):
    return int(n ** 0.5) ** 2 == n


n = int(input())

nums = [int(input()) for _ in range(n)]

count = 0
for n in nums:
    if isSquare(n):
        count += 1

print(count)
