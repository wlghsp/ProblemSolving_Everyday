from collections import deque

N = int(input())

commands = [input() for _ in range(N)]

def process_commands(commands):
    dq = deque()
    for command in commands:
        token = command.split()
        if len(token) == 2:
            if token[0] == 'push_back':
                dq.append(token[1])
            else:
                dq.appendleft(token[1])
        elif len(token) == 1:
            comm = token[0]
            if comm == 'pop_front':
                print(dq.popleft() if dq else -1)
            elif comm == 'pop_back':
                print(dq.pop() if dq else -1)
            elif comm == 'size':
                print(len(dq))
            elif comm == 'empty':
                print(0 if dq else 1)
            elif comm == 'front':
                print(dq[0] if dq else -1)
            elif comm == 'back':
                print(dq[-1] if dq else -1)


process_commands(commands)