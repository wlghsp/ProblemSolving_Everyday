import sys

input = lambda: sys.stdin.readline().rstrip()

nums = [int(input()) for i in range(10)]

print(sum(nums) // 10)
print(max(nums, key=nums.count))