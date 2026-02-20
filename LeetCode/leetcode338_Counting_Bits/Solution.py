from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            # LSB 제거 + LSB 더하기
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.countBits(2))   # Expected: [0, 1, 1]
    print(sol.countBits(5))   # Expected: [0, 1, 1, 2, 1, 2]
