


import sys

input = lambda: sys.stdin.readline().rstrip()


def solve(s):
    cnt = 0
    ans = 'YES'
    for c in s:
        if c =='(':
            cnt+=1
        else:
            if cnt > 0:
                cnt-=1
            else:
                ans = 'NO'
    if cnt > 0:
        ans = 'NO'

    return ans

t = int(input())

for _ in range(t):
    s = input()
    print(solve(s))
