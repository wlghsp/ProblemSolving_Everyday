"""
3
1 2 3


2.0 1

5
183 177 187 170 167

176.8 3

"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
nums = list(map(int, input().split()))
avg_nums = sum(nums) / len(nums)
count = 0

for num in nums:
    if num > avg_nums:
        count += 1

print(f"{avg_nums:.1f}", count)
