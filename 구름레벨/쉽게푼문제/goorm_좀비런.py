"""
7
10 9 18 13 12 5 19

19

5
9 3 5 2 6

9
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))

print(max(nums))
