from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    r = mid # ✅ mid를 포함시킴
            return nums[l]
        return binary_search()

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,1,2])) # 1
    print(sol.findMin([4,5,6,7,0,1,2])) # 0
    print(sol.findMin([3,1,2])) # 1