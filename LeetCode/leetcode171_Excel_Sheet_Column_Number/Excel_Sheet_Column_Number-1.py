class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, c in zip(range(len(columnTitle)), reversed(columnTitle)):
            result += (26 ** i) * (ord(c) - 64)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("ZY"))