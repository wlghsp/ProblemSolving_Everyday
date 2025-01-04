
N = int(input())
commands = [input() for _ in range(N)]

stk = []

for command in commands:
    token = command.split()

    if token[0] == 'push':
        # push X: 정수 X를 스택에 넣는 연산이다.
        stk.append(token[1])
    elif token[0] == 'pop':
        # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(stk.pop() if stk else -1)
    elif token[0] == 'size':
        print(len(stk))
    elif token[0] == 'empty':
        # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        print(0 if stk else 1)
    elif token[0] == 'top':
        # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(stk[-1] if stk else -1)