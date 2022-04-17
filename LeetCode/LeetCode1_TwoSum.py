from typing import List


# 1. 브루트 포스
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] + nums[j]) is target:
#             return [i, j]

def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable_dict = {}

    for i in range(len(nums)):
        value = target - nums[i]

        # get으로 찾으면 None을 돌려주고, []로 찾으면 Key오류 발생 시킴
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])

        hashtable_dict[nums[i]] = i

    return [-1, -1]

print(twoSum([2,7,11,15], 9))