from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search():
            l, r = 0, len(nums) - 1

            while l < r:
                m = l + (r - l) // 2

                if nums[m + 1] > nums[m]:
                    l = m + 1
                else:
                    r = m
            return l
        return search()

if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1])) # 2
