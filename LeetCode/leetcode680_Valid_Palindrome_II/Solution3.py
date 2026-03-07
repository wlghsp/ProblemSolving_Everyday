class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l += 1
            r -= 1
        return True
    
  

if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))    # True
    print(sol.validPalindrome("abca"))   # True (remove 'c')
    print(sol.validPalindrome("abc"))    # False
    print(sol.validPalindrome("a"))      # True
    print(sol.validPalindrome("deeee")) # True (remove 'd')
