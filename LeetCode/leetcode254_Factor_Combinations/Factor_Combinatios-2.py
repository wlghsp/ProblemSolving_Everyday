from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        def backtrack(start, target, path):
            for i in range(start, int(target ** 0.5) + 1):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    backtrack(i, target // i, path + [i])
        backtrack(2, n, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    # print(sol.getFactors(1)) # []
    # print(sol.getFactors(37)) # []
    print(sol.getFactors(12)) # [[2,6],[3,4],[2,2,3]]
    # print(sol.getFactors(32))
    # """
    # [ [2, 16],
    #   [2, 2, 8],
    #   [2, 2, 2, 4],
    #   [2, 2, 2, 2, 2],
    #   [2, 4, 4],
    #   [4, 8]
    # ]
    # """
