from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        res = []
        def comb(picked, start, remain):
            if remain < 0:
                return
            if remain == 0:
                res.append(picked[:])
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]: 
                    continue
                picked.append(candidates[i])
                comb(picked, i + 1, remain - candidates[i])
                picked.pop()

        comb([], 0, target)
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))          # [[1,2,2],[5]]
