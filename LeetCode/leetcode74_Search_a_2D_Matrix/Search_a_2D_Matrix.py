from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, t):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == t:
                    return mid
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        for row in matrix:
            if binary_search(row, target) != -1:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # true
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # false

