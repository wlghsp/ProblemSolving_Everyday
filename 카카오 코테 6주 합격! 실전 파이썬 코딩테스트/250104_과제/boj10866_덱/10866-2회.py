import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dq = deque()

def process_command(command):
    if command.startswith('push'):
        com, number = command.split()
        if com == 'push_front':
            dq.appendleft(int(number))
        else:
            dq.append(int(number))
    elif command == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif command == 'pop_back':
        print(dq.pop() if dq else -1)
    elif command == 'size':
        print(len(dq))
    elif command == 'empty':
        print(0 if dq else 1)
    elif command == 'front':
        print(dq[0] if dq else -1)
    elif command == 'back':
        print(dq[-1] if dq else -1)

for _ in range(N):
    process_command(input())