from collections import deque

N = int(input())

commands = [input() for _ in range(N)]

dq = deque()

for command in commands:
    token = command.split()

    if token[0] == 'push_front':
        # push_front X: 정수 X를 덱의 앞에 넣는다.
        dq.appendleft(token[1])
    elif token[0] == 'push_back':
        # push_back X: 정수 X를 덱의 뒤에 넣는다.
        dq.append(token[1])
    elif token[0] == 'pop_front':
        # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(-1 if len(dq) == 0 else dq.popleft())
    elif token[0] == 'pop_back':
        # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(-1 if len(dq) == 0 else dq.pop())
    elif token[0] == 'size':
        # size: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    elif token[0] == 'empty':
        # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        print(1 if len(dq) == 0 else 0)
    elif token[0] == 'front':
        # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(-1 if len(dq) == 0 else dq[0])
    elif token[0] == 'back':
        # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(-1 if len(dq) == 0 else dq[-1])
