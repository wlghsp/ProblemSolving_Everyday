"""
입
3 3 6
출
1300

입
2 2 2
출
12000

입
6 2 5
출
600
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

list_nums = list(map(int, input().split()))
list_nums.sort()
set_nums = len(set(list_nums))

result = 0
if set_nums == 1:
    result = 10000 + list_nums[0] * 1000
elif set_nums == 2:
    result = 1000 + list_nums[1] * 100
elif set_nums == 3:
    result = list_nums[-1] * 100

print(result)
