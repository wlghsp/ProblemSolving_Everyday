# import sys

# input = sys.stdin.readline

# nums = []
# n = int(input())
# for _ in range(n):
#     nums.append(int(input()))

# nums = sorted(nums)

# for num in nums:
#     print(num)

# 버블 정렬


# nums = []
# n = int(input())
# for _ in range(n):
#     nums.append(int(input()))

# # Bubble sort
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] < nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]

# for num in nums:
#     print(num)


# nums = []
# n = int(input())
# for _ in range(n):
#     nums.append(int(input()))

# # Insert sort
# for i in range(1, len(nums)):
#     while (i > 0) & (nums[i] < nums[i - 1]):
#         nums[i], nums[i - 1] = nums[i - 1], nums[i]
#         i -= 1

# for num in nums:
#     print(num)

nums = [5, 2, 3, 4, 1]


def insertion_sort(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert
    return arr


print(insertion_sort(nums))
