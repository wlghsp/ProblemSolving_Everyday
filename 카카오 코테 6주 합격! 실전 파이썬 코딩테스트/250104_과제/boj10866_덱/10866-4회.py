import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dq = deque()

for _ in range(n):
    string = input().split()
    order = string[0]
    if order == 'push_front':
        dq.appendleft(string[1])
    elif order == 'push_back':
        dq.append(string[1])
    elif order == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif order == 'pop_back':
        print(dq.pop() if dq else -1)
    elif order == 'size':
        print(len(dq))
    elif order == 'empty':
        print(0 if dq else 1)
    elif order == 'front':
        print(dq[0] if dq else -1)
    elif order == 'back':
        print(dq[len(dq) - 1] if dq else -1)