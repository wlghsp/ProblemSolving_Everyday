from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        K = 2
        n = len(prices)
        # dp[k][i] : k번의 거래로 i번째 날까지의 최대 이익
        dp = [[0] * n for _ in range(K + 1)]
        for k in range(1, K + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[k][i] = max(dp[k][i - 1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[k - 1][i] - prices[i])

        return dp[K][n - 1]
