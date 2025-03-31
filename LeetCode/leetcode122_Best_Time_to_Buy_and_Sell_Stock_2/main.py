from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        그리디
        원하는만큼 거래 가능
        오를때마다 판다.
        """

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]


        return max_profit
