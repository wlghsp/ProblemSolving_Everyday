from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.numberOfArithmeticSlices([2, 4, 6, 8, 10]))  # Expected: 7
    # [2,4,6], [4,6,8], [6,8,10], [2,4,6,8], [4,6,8,10], [2,4,6,8,10], [2,6,10]

    print(sol.numberOfArithmeticSlices([7, 7, 7, 7, 7]))   # Expected: 16

    print(sol.numberOfArithmeticSlices([1, 1]))             # Expected: 0
