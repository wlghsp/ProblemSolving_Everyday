from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.permuteUnique([1, 1, 2]))  # [[1,1,2],[1,2,1],[2,1,1]]
    print(s.permuteUnique([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(s.permuteUnique([1]))        # [[1]]
