from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

    def maxProfit1(self, prices: List[int]) -> int:
        ans = 0
        min_val = prices[0]
        for price in prices:
            if price < min_val:
                min_val = price
            ans = max(ans, price - min_val)

        return ans

