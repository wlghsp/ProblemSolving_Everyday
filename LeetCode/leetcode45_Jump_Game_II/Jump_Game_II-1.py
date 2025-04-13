from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * N

        def dfs(pos):
            if pos >= N - 1:
                return 0

            if dp[pos] != float('inf'):
                return dp[pos]

            for step in range(1, nums[pos] + 1):
                if pos + step < N:
                    dp[pos] = min(dp[pos], dfs(pos + step) + 1)

            return dp[pos]

        return dfs(0)



if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4])) # 2
    print(sol.jump([2,3,0,1,4])) # 2


