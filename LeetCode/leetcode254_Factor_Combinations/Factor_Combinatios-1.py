from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        factors = [i for i in range(2, n // 2 + 1) if n % i == 0]
        def calc(nums):
            ret  = 1
            for num in nums:
                ret *= num
            return ret


        def backtrack(picked, start):
            total = calc(picked)
            if len(picked) >= 2 and total == n:
                result.append(picked[:])
                return
            if total > n:
                return

            for i in range(start, len(factors)):
                picked.append(factors[i])
                backtrack(picked, i)
                picked.pop()

        backtrack([], 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.getFactors(1)) # []
    print(sol.getFactors(37)) # []
    print(sol.getFactors(12)) # [[2,6],[3,4],[2,2,3]]
    print(sol.getFactors(32))
    """
    [ [2, 16],
      [2, 2, 8],
      [2, 2, 2, 4],
      [2, 2, 2, 2, 2],
      [2, 4, 4],
      [4, 8]
    ]
    """
