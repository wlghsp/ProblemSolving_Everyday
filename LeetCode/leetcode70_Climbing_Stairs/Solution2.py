class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == "__main__":
    sol = Solution()

    print(sol.climbStairs(2))  # Expected: 2
    # Explanation: 1+1, 2

    print(sol.climbStairs(3))  # Expected: 3
    # Explanation: 1+1+1, 1+2, 2+1

    print(sol.climbStairs(1))  # Expected: 1

    print(sol.climbStairs(5))  # Expected: 8
