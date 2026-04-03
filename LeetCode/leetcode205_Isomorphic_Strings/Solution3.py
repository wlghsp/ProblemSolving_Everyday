"""
205. Isomorphic Strings (Easy)
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for a, b in zip(s, t):
            if a in dict1 and dict1[a] != b:
                return False
            if b in dict2 and dict2[b] != a:
                return False
            dict1[a] = b
            dict2[b] = a
           
        return True
            

if __name__ == "__main__":
    sol = Solution()

    print(sol.isIsomorphic("egg", "add"))    # Expected: True
    print(sol.isIsomorphic("foo", "bar"))    # Expected: False
    print(sol.isIsomorphic("paper", "title")) # Expected: True
    print(sol.isIsomorphic("badc", "baba"))  # Expected: False
