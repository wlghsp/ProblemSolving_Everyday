class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        curr = ""
        curr_num = 0
        for c in s:
            if c == "]":
                prevNum, prev_str = stk.pop()
                curr = prev_str + prevNum * curr
            elif c == "[":
                stk.append((curr_num, curr))
                curr_num = 0
                curr = ""
            else:
                if c.isdigit():
                    curr_num = curr_num * 10 + int(c)
                else:
                    curr += c 
        return curr

if __name__ == "__main__":
    sol = Solution()

    # Example 1: s = "3[a]2[bc]"
    # Expected: "aaabcbc"
    print(sol.decodeString("3[a]2[bc]"))

    # Example 2: s = "3[a2[c]]"
    # Expected: "accaccacc"
    print(sol.decodeString("3[a2[c]]"))

    # Example 3: s = "2[abc]3[cd]ef"
    # Expected: "abcabccdcdcdef"
    print(sol.decodeString("2[abc]3[cd]ef"))

    print(sol.decodeString("100[leetcode]"))