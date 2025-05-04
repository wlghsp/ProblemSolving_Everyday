from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       stk = []
       for c in tokens:
           if c in ['+', '-', '*', '/']:
                b, a = stk.pop(), stk.pop()
                if c == '+':
                    res = a + b
                elif c == '-':
                    res = a - b
                elif c == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stk.append(res)
           else:
               stk.append(int(c))
       return stk[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"])) # 9
    print(sol.evalRPN(["4","13","5","/","+"])) # 6
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
    print(sol.evalRPN(["3","11","+","5","-"])) # 9

