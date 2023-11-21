from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = prices[0]
        for price in prices:
            if price < min_val:
                min_val = price
            ans = max(ans, price - min_val)

        return ans

