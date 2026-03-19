class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        for c in s:
            word[c] = word.get(c, 0) + 1
        for c in t:
            word[c] = word.get(c, 0) - 1
        return all(v == 0 for v in word.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("a", "ab"))             # False
