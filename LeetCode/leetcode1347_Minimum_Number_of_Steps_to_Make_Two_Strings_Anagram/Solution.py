class Solution:
    def minSteps(self, s: str, t: str) -> int:
        rec = {}
        for a, b in zip(s, t):
            rec[a] = rec.get(a, 0) + 1
            rec[b] = rec.get(b, 0) - 1
        return sum([v for v in rec.values() if v > 0])


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSteps("bab", "aba"))       # 1
    print(sol.minSteps("leetcode", "practice"))  # 5
    print(sol.minSteps("anagram", "mangaar"))    # 0
