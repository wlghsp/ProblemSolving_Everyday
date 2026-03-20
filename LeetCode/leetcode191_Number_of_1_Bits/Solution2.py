class Solution:
    def hammingWeight(self, n: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.hammingWeight(11))   # Expected: 3  (0b1011)
    print(sol.hammingWeight(128))  # Expected: 1  (0b10000000)
    print(sol.hammingWeight(2147483645))  # Expected: 30
