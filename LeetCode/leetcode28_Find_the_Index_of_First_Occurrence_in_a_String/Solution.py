class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test 1: haystack = "sadbutsad", needle = "sad" → 0
    print(sol.strStr("sadbutsad", "sad"))  # 0

    # Test 2: haystack = "leetcode", needle = "leeto" → -1
    print(sol.strStr("leetcode", "leeto"))  # -1

    # Test 3: haystack = "a", needle = "a" → 0
    print(sol.strStr("a", "a"))  # 0

    # Test 4: haystack = "hello", needle = "ll" → 2
    print(sol.strStr("hello", "ll"))  # 2
