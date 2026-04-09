from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        while len(g) > i and len(s) > j:
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1: Expected 1
    print(sol.findContentChildren([1, 2, 3], [1, 1]))

    # Example 2: Expected 2
    print(sol.findContentChildren([1, 2], [1, 2, 3]))
