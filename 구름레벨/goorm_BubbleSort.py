import sys

input = sys.stdin.readline


def bubble_sort(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                count += 1
    # for i in range(len(nums)):
    #     for j in range(len(nums) - 1 - i):
    #         if nums[j] > nums[j + 1]:
    #             nums[j + 1], nums[j] = nums[j], nums[j + 1]
    #             count += 1
    return nums


n = int(input())
nums = list(map(int, input().split()))
print(*bubble_sort(nums), end="")
print(" ")
