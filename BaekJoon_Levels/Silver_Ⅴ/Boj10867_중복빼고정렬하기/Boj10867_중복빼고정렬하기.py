

import sys
input = lambda : sys.stdin.readline().rstrip()


N = int(input())

nums = sorted(set(map(int, input().split())))
print(*nums)
