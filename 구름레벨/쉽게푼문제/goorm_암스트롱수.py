"""
100 500

153 370 371 407

100 300

153

"""


import sys

input = lambda: sys.stdin.readline().rstrip()

nums = list(input().split())

start = int(nums[0])

end = int(nums[1])

result = []
for i in range(start, end + 1):
    i_str = list(str(i))
    sumofThree = 0
    for j in i_str:
        sumofThree += int(j) ** 3
    if sumofThree == int(i):
        result.append(i)

print(*result, end=" ")
