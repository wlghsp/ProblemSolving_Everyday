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
    print(sol.validPalindrome("aba"))    # True
    print(sol.validPalindrome("abca"))   # True
    print(sol.validPalindrome("abc"))    # False
