class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = solution.convert(s1, numRows1)
    print(f"Test 1: '{result1}'")  # Expected: "PAHNAPLSIIGYIR"

    # Test case 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    result2 = solution.convert(s2, numRows2)
    print(f"Test 2: '{result2}'")  # Expected: "PINALSIGYAHRPI"

    # Test case 3
    s3 = "A"
    numRows3 = 1
    result3 = solution.convert(s3, numRows3)
    print(f"Test 3: '{result3}'")  # Expected: "A"

    # Test case 4
    s4 = "AB"
    numRows4 = 1
    result4 = solution.convert(s4, numRows4)
    print(f"Test 4: '{result4}'")  # Expected: "AB"

    # Test case 5
    s5 = "ABCD"
    numRows5 = 2
    result5 = solution.convert(s5, numRows5)
    print(f"Test 5: '{result5}'")  # Expected: "ACBD"
