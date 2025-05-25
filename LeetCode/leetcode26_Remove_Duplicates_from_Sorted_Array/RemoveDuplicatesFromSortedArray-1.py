from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[right] = nums[left]
        return left + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2])) # 2
