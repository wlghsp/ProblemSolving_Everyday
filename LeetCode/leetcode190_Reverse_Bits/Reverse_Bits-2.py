class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = result << 1 | n & 1
            n >>= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596)) # 964176192

