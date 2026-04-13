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

    print(sol.isIsomorphic("egg", "add"))   # True
    print(sol.isIsomorphic("foo", "bar"))   # False
    print(sol.isIsomorphic("paper", "title"))  # True
    print(sol.isIsomorphic("ab", "aa"))     # False
