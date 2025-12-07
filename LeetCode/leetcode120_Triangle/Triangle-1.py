from typing import List


class Solution:
    def minimumTotalTopDown(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]

            if (row, col) in memo:
                return memo[(row, col)]

            left = dfs(row + 1, col)
            right = dfs(row + 1, col + 1)

            memo[(row, col)] = triangle[row][col] + min(left, right)
            return memo[(row, col)]

        return dfs(0, 0)


    def minimumTotalBottomUp(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )
        return triangle[0][0]





if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotalTopDown([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
    print(sol.minimumTotalTopDown([[-10]]))  # -10
