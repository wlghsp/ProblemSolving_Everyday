class Solution:
    def decodeString(self, s: str) -> str:
        pass


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
