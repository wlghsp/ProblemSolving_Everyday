class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) != 2:
            return False

        a, b = diff[0], diff[1]
        s_list, g_list = list(s), list(goal)
        s_list[b], s_list[a] = s_list[a], s_list[b]
        return ''.join(s_list) == ''.join(g_list)


if __name__ == "__main__":
    sol = Solution()
    print(sol.buddyStrings("ab", "ba")) # true
    print(sol.buddyStrings("ab", "ab")) # false
    print(sol.buddyStrings("aaaaaaabc", "aaaaaaacb")) # true