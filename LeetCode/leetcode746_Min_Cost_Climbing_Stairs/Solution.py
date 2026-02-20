from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[- 1], dp[- 2])


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [10,15,20] → 15
    print(sol.minCostClimbingStairs([10, 15, 20]))  # 15

    # Test 2: [1,100,1,1,1,100,1,1,100,1] → 6
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
