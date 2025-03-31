from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        그리디
        한번만 사고 팔 수 있음
        지금가격 - 이전까지의 최소 가격 = 현재 가능한 최대 이익
        """
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)

        return max_profit
