class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
    print(sol.minRemoveToMakeValid("a)b(c)d"))        # "ab(c)d"
    print(sol.minRemoveToMakeValid("))(("))            # ""
