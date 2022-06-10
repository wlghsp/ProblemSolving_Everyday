import sys
input = lambda : sys.stdin.readline().rstrip()


nums = [i for i in map(int, input().split())]

for i in range(5):
    for j in range(5 - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(*nums)

