from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in num_dict:
                return [num_dict.get(other), i]
            num_dict[nums[i]] = i
        return []



if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9)) # [0, 1]
    print(sol.twoSum([3, 2, 4], 6)) # [1, 2]
    print(sol.twoSum([3, 3], 6)) # [0, 1]