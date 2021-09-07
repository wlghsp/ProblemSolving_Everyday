"""
7
49 62 18 37 75 33 85

85 7

9
3 29 38 12 57 74 40 99 61

99 8
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))

print(max(nums), nums.index(max(nums)) + 1)
