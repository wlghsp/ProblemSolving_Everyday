
import sys
input = lambda : sys.stdin.readline().rstrip()


s = input()

stk = []
def solve(s):
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            stk.append(c)
        else:
            if not stk: return "NO"
            stk.pop()
    return "YES" if not stk else "NO"

print(solve(s))