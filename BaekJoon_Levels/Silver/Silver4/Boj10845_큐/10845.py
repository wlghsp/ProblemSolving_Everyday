import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

queue = deque()

def process_command(command):
    if command.startswith("push"):
        _, num = command.split()
        queue.append(int(num))
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == "pop":
        print(queue.popleft() if queue else -1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(0 if queue else 1)
    elif command == 'back':
        print(queue[-1] if queue else -1)


N = int(input())

for i in range(N):
    command = input()
    process_command(command)