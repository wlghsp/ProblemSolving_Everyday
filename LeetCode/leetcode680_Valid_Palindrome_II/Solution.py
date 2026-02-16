class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1
            r -= 1    

        return True
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: s = "aba"
    print(sol.validPalindrome("aba"))  # Expected: True
    # Explanation: Already a palindrome

    # Test 2: s = "abca"
    print(sol.validPalindrome("abca"))  # Expected: True
    # Explanation: Delete 'c' or 'b' → "aba" or "aca" (both palindromes)

    # Test 3: s = "abc"
    print(sol.validPalindrome("abc"))  # Expected: False
    # Explanation: Cannot form palindrome by deleting at most 1 character

    # Test 4: s = "racecar"
    print(sol.validPalindrome("racecar"))  # Expected: True
    # Explanation: Already a palindrome

    # Test 5: s = "abccdba"
    print(sol.validPalindrome("abccdba"))  # Expected: True
    # Explanation: Delete one 'c' → "abcdba" is palindrome

    # Test 6: s = "tebbem"
    print(sol.validPalindrome("tebbem"))  # Expected: False
