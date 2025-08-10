from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = global_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            global_max = max(cur_max, global_max)
        return global_max

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
