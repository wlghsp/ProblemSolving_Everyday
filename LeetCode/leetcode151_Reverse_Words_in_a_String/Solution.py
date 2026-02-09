class Solution:
    def reverseWords(self, s: str) -> str:
        # 문자열을 리스트로 변환 (Python 문자열은 immutable)
        chars = list(s)
        
        # 1. 전체 뒤집기
        self.reverse(chars, 0, len(chars) - 1)
        
        # 2. 각 단어 뒤집기
        self.reverseEveryWords(chars)
        
        # 3. 공백 정리
        result = self.cleanSpaces(chars)
        
        return ''.join(result)
    
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
    def reverseEveryWords(self, chars):
        n = len(chars)
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                self.reverse(chars, start, end - 1)
                start = end + 1
    def cleanSpaces(self, chars):
        n = len(chars)
        result = []
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

    # Test case 5
    s5 = "Alice does not even like bob"
    result5 = solution.reverseWords(s5)
    print(f"Test 5: '{result5}'")  # Expected: "bob like even not does Alice"
