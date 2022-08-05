

import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())


for _ in range(n):
    p = int(input())
    maxVal = 0
    maxPlayer = ''
    for _ in range(p):
        c, name = input().split()
        if maxVal < int(c):
            maxVal = int(c)
            maxPlayer = name
    print(maxPlayer)