from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0
        for p in prices[1:]:
            min_p = min(p, min_p)
            max_profit = max(max_profit, p - min_p)
        return max_profit

if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))      # Expected: 0
