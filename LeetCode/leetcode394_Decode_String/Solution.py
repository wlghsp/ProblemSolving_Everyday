class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        current_string = ""
        current_num = 0
        for c in s:
            if c == '[':
                # 1. [ 이면 (이전 숫자, 이전 문자열) 스택 저장 후 초기화
                stk.append((current_num, current_string))
                current_string = ""
                current_num = 0
            elif c == ']':
                prev_num, prev_string  = stk.pop()
                current_string = prev_string + current_string * prev_num
            else:
                if c.isdigit():
                    current_num = current_num * 10 + int(c)
                else:
                    current_string += c

        return current_string

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.decodeString("3[a]2[bc]")
    print(f"Test 1: {result1}")  # Expected: "aaabcbc"

    # Test case 2
    result2 = solution.decodeString("3[a2[c]]")
    print(f"Test 2: {result2}")  # Expected: "accaccacc"

    # Test case 3
    result3 = solution.decodeString("2[abc]3[cd]ef")
    print(f"Test 3: {result3}")  # Expected: "abcabccdcdcdef"

    # Test case 4
    result4 = solution.decodeString("100[leetcode]")
    print(f"Test 4: {result4[:30]}...")  # Expected: "leetcodeleetcode..."
