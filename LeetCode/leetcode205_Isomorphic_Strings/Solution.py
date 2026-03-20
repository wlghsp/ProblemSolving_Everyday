class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word = {}
        word1 = {}
        for a, b in zip(s, t):
            if a in word and word[a] != b:
                return False
            if b in word1 and word1[b] != a:
                return False
            word[a] = b
            word1[b] = a
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))    # True
    print(sol.isIsomorphic("foo", "bar"))    # False
    print(sol.isIsomorphic("paper", "title"))  # True
    print(sol.isIsomorphic("badc", "baba"))  # False

"""
b b
a a
d b
c a

p t
a i
p t
e l
r e

"""
