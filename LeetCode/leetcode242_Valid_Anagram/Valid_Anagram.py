class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1


        return all(c == 0 for c in count.values())

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.isAnagram("anagram", "nagaram"))  # True

    # Example 2
    print(sol.isAnagram("rat", "car"))  # False

    # Example 3
    print(sol.isAnagram("listen", "silent"))  # True

    # Example 4
    print(sol.isAnagram("a", "ab"))  # False

    # Example 5
    print(sol.isAnagram("", ""))  # True
