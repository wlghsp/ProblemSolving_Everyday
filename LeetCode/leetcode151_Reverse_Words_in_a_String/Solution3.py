class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        # 1. 전체 뒤집기
        self.reverse(chars, 0, len(chars) - 1)
        # 2. 각 단어 뒤집기
        self.reverse_words(chars)
        # 3. 공백 제거
        result = self.remove_empty_space(chars)
        return ''.join(result)

    def reverse(self, chars, start, end):
        left, right = start, end

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
    def reverse_words(self, chars):
        start = 0
        n = len(chars)
        while start < n:
            for end in range(start, n + 1):
                if end == n or chars[end] == ' ':
                    self.reverse(chars, start, end - 1)
                    start = end + 1

    def remove_empty_space(self, chars):
        result = []
        i = 0
        n = len(chars)
        while i < n:
            if chars[i] != ' ':
                if result:
                    result.append(' ')
                while i < n and chars[i] != ' ':
                    result.append(chars[i])
                    i += 1
            else:
                i += 1
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.reverseWords("the sky is blue")
    print(f"Test 1: '{result1}'")  # Expected: "blue is sky the"

    # Test case 2
    result2 = solution.reverseWords("  hello world  ")
    print(f"Test 2: '{result2}'")  # Expected: "world hello"

    # Test case 3
    result3 = solution.reverseWords("a good   example")
    print(f"Test 3: '{result3}'")  # Expected: "example good a"

    # Test case 4
    result4 = solution.reverseWords("  Bob    Loves  Alice   ")
    print(f"Test 4: '{result4}'")  # Expected: "Alice Loves Bob"
