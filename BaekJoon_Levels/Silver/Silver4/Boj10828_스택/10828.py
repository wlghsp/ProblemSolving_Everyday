import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

stk = []

def process_command(command):
    if command.startswith('push'):
        _, num = command.split()
        stk.append(int(num))
    elif command == 'top':
        print(stk[-1] if stk else -1)
    elif command == 'pop':
        print(stk.pop() if stk else -1)
    elif command == 'size':
        print(len(stk))
    elif command == 'empty':
        print(0 if stk else 1)

for _ in range(N):
    command = input()
    process_command(command)