from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(cur, open_cnt, close_cnt):
            if len(cur) == 2 * n:
                result.append(cur)
                return
            if open_cnt < n:
                dfs(cur + "(", open_cnt + 1, close_cnt)
            if close_cnt < open_cnt:
                dfs(cur + ")", open_cnt, close_cnt + 1)

        dfs("", 0, 0)

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
