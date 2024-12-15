
import sys
input = lambda : sys.stdin.readline().rstrip()

nums = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        nums.append(num)

if not nums:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))