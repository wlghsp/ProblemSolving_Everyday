from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(p - min_price, max_profit)
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(f"Test 1: {result1}")  # Expected: 5

    # Test case 2
    result2 = solution.maxProfit([7, 6, 4, 3, 1])
    print(f"Test 2: {result2}")  # Expected: 0

    # Test case 3
    result3 = solution.maxProfit([2, 4, 1])
    print(f"Test 3: {result3}")  # Expected: 2

    # Test case 4
    result4 = solution.maxProfit([1])
    print(f"Test 4: {result4}")  # Expected: 0
