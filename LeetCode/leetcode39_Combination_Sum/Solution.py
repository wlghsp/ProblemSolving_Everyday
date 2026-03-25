from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def comb(nums, start, remain):
            if remain < 0: 
                return
            if remain == 0:
                res.append(nums[:])
                return
            for i in range(start, n):
                nums.append(candidates[i])
                comb(nums, i, remain - candidates[i])
                nums.pop()
            
        comb([], 0, target)
        return res
        


if __name__ == "__main__":
    sol = Solution()

    print(sol.combinationSum([2, 3, 6, 7], 7))   # [[2,2,3],[7]]
    print(sol.combinationSum([2, 3, 8], 8))        # [[2,2,2,2],[2,3,3],[8] ... wait no: [[2,2,2,2],[2,3,3],[8]] → actually [[2,2,2,2],[2,3,3],[3,5] no]
    # Expected: [[2,2,2,2],[2,3,3],[8]]
    print(sol.combinationSum([2], 1))              # []
