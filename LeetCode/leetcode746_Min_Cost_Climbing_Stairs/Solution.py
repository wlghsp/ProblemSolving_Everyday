class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.minCostClimbingStairs([10, 15, 20]))  # Expected: 15
    # Explanation: Start at index 1, pay 15, jump 2 steps to top

    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6
    # Explanation: 1+1+1+1+1+1 = 6 (stepping on cheap steps)
