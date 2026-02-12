class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(s)
        # 1. 전체 뒤집기
        self.reverse(chars, 0, n - 1)
        # 2. 각 단어 뒤집기
        self.reverse_words(chars)
        # 3. 공백 정리 
        result = self.remove_empty(chars)
        return ''.join(result)
    
    def reverse(self, chars, start, end):
        left, right = start, end

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def reverse_words(self, chars):
        n = len(chars)
        start = 0
        while start < n:
            for end in range(start, n + 1):
                if end == n or chars[end] == ' ':
                    self.reverse(chars, start, end - 1)
                    start = end + 1

    def remove_empty(self, chars):
        result = []
        n = len(chars)
        i = 0
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
