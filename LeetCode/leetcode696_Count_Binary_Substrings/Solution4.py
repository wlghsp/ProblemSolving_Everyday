from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        curr_cnt = 1
        curr_str = s[0]
        for c in s[1:]:
            if curr_str == c:
                curr_cnt += 1
            else:
                result += min(prev, curr_cnt)
                prev = curr_cnt
                curr_cnt = 1
                curr_str = c
        result += min(prev, curr_cnt)
        return result

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countBinarySubstrings("00110011"))  # Expected: 6
    # "0011", "01", "1100", "10", "0011", "01"

    # Example 2
    print(sol.countBinarySubstrings("10101"))  # Expected: 4
    # "10", "01", "10", "01"
