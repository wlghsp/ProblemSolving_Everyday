class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            cnt += 1 if n & 1 == 1 else 0
            n >>= 1
        return cnt

if __name__ == "__main__":
    sol = Solution()

    print(sol.hammingWeight(11))   # Expected: 3  (1011)
    print(sol.hammingWeight(128))  # Expected: 1  (10000000)
    print(sol.hammingWeight(2147483645))  # Expected: 30
