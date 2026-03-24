class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        right = {}
        left = {}
        for a, b in zip(s, t):
            if a in right and right[a] != b:
                return False
            if b in left and left[b] != a:
                return False
            right[a] = b
            left[b] = a
        return True

if __name__ == "__main__":
    sol = Solution()

    # Test 1: "egg", "add" -> True
    print(sol.isIsomorphic("egg", "add"))

    # Test 2: "foo", "bar" -> False
    print(sol.isIsomorphic("foo", "bar"))

    # Test 3: "paper", "title" -> True
    print(sol.isIsomorphic("paper", "title"))

    # Test 4: "badc", "baba" -> False
    print(sol.isIsomorphic("badc", "baba"))
