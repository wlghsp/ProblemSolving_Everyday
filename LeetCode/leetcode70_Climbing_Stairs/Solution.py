class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(3, n + 1):
            res = a + b
            a = b
            b = res
        return b


if __name__ == "__main__":
    sol = Solution()

    # Test 1: n = 2
    print(sol.climbStairs(2))  # Expected: 2
    # Explanation: 1+1, 2

    # Test 2: n = 3
    print(sol.climbStairs(3))  # Expected: 3
    # Explanation: 1+1+1, 1+2, 2+1

    # Test 3: n = 4
    print(sol.climbStairs(4))  # Expected: 5
    # Explanation: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2

    # Test 4: n = 5
    print(sol.climbStairs(5))  # Expected: 8

    # Test 5: n = 1
    print(sol.climbStairs(1))  # Expected: 1
