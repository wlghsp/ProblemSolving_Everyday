from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5)) # 2
