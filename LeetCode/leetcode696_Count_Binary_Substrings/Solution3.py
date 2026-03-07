class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        prev = 0
        curr = s[0]
        curr_count = 1
        for i in range(1, n):
            if s[i] == curr:
                curr_count += 1
            else:
                result += min(prev, curr_count)
                curr = s[i]
                prev = curr_count
                curr_count = 1
        result += min(prev, curr_count)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBinarySubstrings("00110011"))  # 6
    print(sol.countBinarySubstrings("10101"))      # 4
    print(sol.countBinarySubstrings("00110"))      # 3
