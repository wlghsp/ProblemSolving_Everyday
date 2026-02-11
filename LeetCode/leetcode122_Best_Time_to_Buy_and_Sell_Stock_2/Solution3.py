from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(f"Test 1: {result1}")  # Expected: 7

    # Test case 2
    result2 = solution.maxProfit([1, 2, 3, 4, 5])
    print(f"Test 2: {result2}")  # Expected: 4

    # Test case 3
    result3 = solution.maxProfit([7, 6, 4, 3, 1])
    print(f"Test 3: {result3}")  # Expected: 0
