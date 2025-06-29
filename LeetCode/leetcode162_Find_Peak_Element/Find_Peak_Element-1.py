from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] < nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
            return l

        return search()


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1])) # 2
