class Solution:
    def reverseWords(self, s: str) -> str:
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "the sky is blue"
    result1 = solution.reverseWords(s1)
    print(f"Test 1: '{result1}'")  # Expected: "blue is sky the"

    # Test case 2
    s2 = "  hello world  "
    result2 = solution.reverseWords(s2)
    print(f"Test 2: '{result2}'")  # Expected: "world hello"

    # Test case 3
    s3 = "a good   example"
    result3 = solution.reverseWords(s3)
    print(f"Test 3: '{result3}'")  # Expected: "example good a"

    # Test case 4
    s4 = "  Bob    Loves  Alice   "
    result4 = solution.reverseWords(s4)
    print(f"Test 4: '{result4}'")  # Expected: "Alice Loves Bob"

    # Test case 5
    s5 = "Alice does not even like bob"
    result5 = solution.reverseWords(s5)
    print(f"Test 5: '{result5}'")  # Expected: "bob like even not does Alice"
