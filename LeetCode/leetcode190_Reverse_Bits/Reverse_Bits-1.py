class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # result는 왼쪽으로 비트 이동하고 n 의 마지막 비트를 붙여줌
            result = (result << 1) | (n & 1)
            n >>= 1 # 오른쪽으로 비트 이동
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596)) # 964176192

