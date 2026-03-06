from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        curr = 0
        for i in range(2, n):
            curr = cost[i] + min(prev2, prev1)
            prev2, prev1 = prev1, curr
            
        return min(prev2, prev1)

if __name__ == "__main__":
    s = Solution()

    # Example 1: cost = [10,15,20] → 15
    print(s.minCostClimbingStairs([10, 15, 20]))  # Expected: 15

    # Example 2: cost = [1,100,1,1,1,100,1,1,100,1] → 6
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6

    # Edge: 2개 원소
    print(s.minCostClimbingStairs([0, 0]))  # Expected: 0
