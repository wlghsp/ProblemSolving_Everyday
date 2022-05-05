from typing import List


# 1. Brute force
# def searchInsert(nums: List[int], target: int) -> int:
#     index = 0
#
#     while index < len(nums):
#         if target <= nums[index]:
#             break
#
#         index += 1
#
#     return index

def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low+high) / 2)

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid -1

    return low


print(searchInsert([1,3,5,6], 2)) # 1
