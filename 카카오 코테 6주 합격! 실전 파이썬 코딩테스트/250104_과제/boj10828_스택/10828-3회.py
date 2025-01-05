import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
commands = [input() for _ in range(N)]

stk = []

def handle_command(command):
    token = command.split()

    if token[0] == "push":
        stk.append(token[1])
    elif token[0] == "pop":
        print(stk.pop() if stk else -1)
    elif token[0] == "size":
        print(len(stk))
    elif token[0] == "empty":
        print(0 if stk else 1)
    elif token[0] == "top":
        print(stk[-1] if stk else -1)

for command in commands:
    handle_command(command)

