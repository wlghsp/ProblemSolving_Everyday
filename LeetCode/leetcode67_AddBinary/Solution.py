class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2)) # 현재 자리
            carry = total // 2 # 올림

        return ''.join(reversed(result))


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.addBinary("11", "1")
    print(f"Test 1: {result1}")  # Expected: "100"

    # Test case 2
    result2 = solution.addBinary("1010", "1011")
    print(f"Test 2: {result2}")  # Expected: "10101"

    # Test case 3
    result3 = solution.addBinary("0", "0")
    print(f"Test 3: {result3}")  # Expected: "0"

    # Test case 4
    result4 = solution.addBinary("1", "111")
    print(f"Test 4: {result4}")  # Expected: "1000"
