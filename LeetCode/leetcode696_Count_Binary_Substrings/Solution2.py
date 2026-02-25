from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        curr = 1
        ch = s[0]
        for c in s[1:]:
            if ch == c:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1
                ch = c
        result += min(prev, curr)
        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.countBinarySubstrings("00110011"))   # 6
    print(sol.countBinarySubstrings("10101"))       # 4
    print(sol.countBinarySubstrings("0011"))        # 2
