

import sys
input = lambda : sys.stdin.readline().rstrip()


n, m = map(int, input().split())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return


