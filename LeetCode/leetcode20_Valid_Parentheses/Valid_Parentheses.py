class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pair = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pair: # 닫힌 괄호
                # 닫힌 괄호가 들어왔는데 스택이 비어 있거나
                # 스택에 들어 있는 여는 괄호가 다른 괄호라면 invalid
                if not stk or stk[-1] != pair[c]:
                        return False
                stk.pop()
            else:
                stk.append(c)

        return not stk

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()")) # true
    print(sol.isValid("()[]{}")) # true
    print(sol.isValid( "(]")) # false

