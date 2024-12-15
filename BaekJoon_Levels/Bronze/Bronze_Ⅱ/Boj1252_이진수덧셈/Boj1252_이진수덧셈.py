

import sys
input = lambda : sys.stdin.readline().rstrip()

nums = input().split()
print(bin(int(nums[0], 2) + int(nums[1], 2))[2:])
