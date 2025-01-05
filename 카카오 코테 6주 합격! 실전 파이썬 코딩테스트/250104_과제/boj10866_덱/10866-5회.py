import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dq = deque()

for _ in range(n):
    command = input()
    order = command.split()
    if len(order) == 2:
        if order[0].endswith('front'):
            dq.appendleft(int(order[1]))
        else:
            dq.append(int(order[1]))
    elif order[0].startswith('pop'):
        if order[0].endswith('front'):
            print(dq.popleft() if dq else -1)
        else:
            print(dq.pop() if dq else -1)
    elif order[0] == 'size':
        print(len(dq))
    elif order[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)