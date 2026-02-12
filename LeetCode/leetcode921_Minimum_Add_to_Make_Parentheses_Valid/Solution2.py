class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for c in s:
            if c == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)

        return len(stk)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.minAddToMakeValid("())")
    print(f"Test 1: {result1}")  # Expected: 1

    # Test case 2
    result2 = solution.minAddToMakeValid("(((")
    print(f"Test 2: {result2}")  # Expected: 3

    # Test case 3
    result3 = solution.minAddToMakeValid("()")
    print(f"Test 3: {result3}")  # Expected: 0

    # Test case 4
    result4 = solution.minAddToMakeValid("()))((")
    print(f"Test 4: {result4}")  # Expected: 4

    # Test case 5
    result5 = solution.minAddToMakeValid("")
    print(f"Test 5: {result5}")  # Expected: 0
