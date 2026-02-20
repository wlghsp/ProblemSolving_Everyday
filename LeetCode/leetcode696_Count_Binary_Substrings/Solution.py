class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group_cnt = []
        curr = s[0]
        cnt = 1
        for i in range(1, len(s)):
            c = s[i]
            if curr == c:
                cnt += 1
            else:
                group_cnt.append(cnt)
                cnt = 1
                curr = c
                
        group_cnt.append(cnt)
        result = 0
        for i in range(len(group_cnt) - 1):
            result += min(group_cnt[i], group_cnt[i + 1])
        return result
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBinarySubstrings("00110011"))  # 6
    print(sol.countBinarySubstrings("10101"))     # 4
