import sys
input = lambda : sys.stdin.readline().rstrip()

nums = map(int, input().split(","))
print(sum(nums))