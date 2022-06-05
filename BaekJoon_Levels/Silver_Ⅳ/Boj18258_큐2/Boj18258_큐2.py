


import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dq = deque([])
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        print(dq.popleft() if dq else -1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(0 if dq else 1)
    elif command[0] == 'front':
        print(dq[0] if dq else -1)
    elif command[0] == 'back':
        print(dq[-1] if dq else -1)
