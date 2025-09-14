from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] += dp[0][i - 1]
        for j in range(1, n):
            dp[0][j] += dp[0][j - 1]

        return min(min(row) for row in dp)



if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7