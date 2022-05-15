

import sys
input = lambda : sys.stdin.readline().rstrip()

def solve(string):
    stk = []
    for c in list(string):
        if c == "(":
            stk.append(c)
        elif len(stk) == 0:
            return "NO"
        else:
            stk.pop()

    return "YES" if len(stk) == 0 else "NO"


T = int(input())
for i in range(T):
    print(solve(input()))

