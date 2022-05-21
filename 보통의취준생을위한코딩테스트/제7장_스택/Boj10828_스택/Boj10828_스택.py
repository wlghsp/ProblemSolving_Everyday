


import sys

input = lambda : sys.stdin.readline().rstrip()

stk = []
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        stk.append(command[1])
    elif command[0] == 'pop':
        print(-1 if not stk else stk.pop())
    elif command[0] == 'size':
        print(len(stk))
    elif command[0] == 'empty':
        print(0 if stk else 1)
    elif command[0] == 'top':
        print(-1 if not stk else stk[-1])