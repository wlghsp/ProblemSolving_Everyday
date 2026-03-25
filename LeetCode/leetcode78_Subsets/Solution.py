from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def comb(picked, start, length):
            if len(picked) == length:
                res.append(picked[:])
                return
            for i in range(start, n):
                picked.append(nums[i])
                comb(picked, i + 1, length)
                picked.pop()
        
        for length in range(n + 1):
            comb([], 0, length)

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.subsets([1, 2, 3]))  # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    print(sol.subsets([0]))        # [[], [0]]
