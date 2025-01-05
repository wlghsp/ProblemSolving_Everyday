import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stk = []
for i in range(n):
    command = input()
    command = command.split()
    if len(command) == 2:
        stk.append(command[1])
    elif command[0].startswith('p'):
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif command[0].startswith('s'):
        print(len(stk))
    elif command[0].startswith('e'):
        if len(stk) != 0:
            print(0)
        else:
            print(1)
    else:
        if len(stk) > 0:
            print(stk[len(stk) - 1])
        else:
            print(-1)