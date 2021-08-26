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

def issquare(n):
    return int(n ** 0.5)**2 == n

n = int(input())

nums = [int(input()) for _ in range(n)]

count = 0
for n in nums:
    if issquare(n):
        count += 1

print(count) 
