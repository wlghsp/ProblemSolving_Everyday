import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dq = deque()

def process_command(command):
    if command.startswith("push_front"):
        _, num = command.split()
        dq.appendleft(int(num))
    elif command.startswith("push_back"):
        _, num = command.split()
        dq.append(int(num))
    elif command == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif command == 'pop_back':
        print(dq.pop() if dq else -1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(0 if dq else 1)
    elif command == 'front':
        print(dq[0] if dq else -1)
    elif command == 'back':
        print(dq[-1] if dq else -1)


N = int(input())

for i in range(N):
    command = input()
    process_command(command)