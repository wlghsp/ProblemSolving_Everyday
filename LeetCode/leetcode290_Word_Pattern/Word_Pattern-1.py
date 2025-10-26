class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_p = list(pattern)
        list_s = s.split()

        if len(list_p) != len(list_s):
            return False

        if len(set(list_p)) != len(set(list_s)):
            return False

        map_p = {}
        for i in range(len(list_p)):
            if list_p[i] in map_p and map_p[list_p[i]] != list_s[i]:
                return False
            map_p[list_p[i]] = list_s[i]

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba",  "dog cat cat dog")) # true
    print(sol.wordPattern("abba",  "dog cat cat fish")) # false
    print(sol.wordPattern("aaaa",  "dog cat cat dog")) # false