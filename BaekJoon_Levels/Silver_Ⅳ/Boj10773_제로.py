


import sys

input = lambda : sys.stdin.readline().rstrip()

stk = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))