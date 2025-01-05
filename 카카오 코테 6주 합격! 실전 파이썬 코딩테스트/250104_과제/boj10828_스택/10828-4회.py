import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

stk = []

def operate_input(input_string):
    if input_string.startswith('push'):
        _, num = input_string.split()
        stk.append(num)
    elif input_string.startswith('pop'):
        print(stk.pop() if stk else -1)
    elif input_string.startswith('size'):
        print(len(stk))
    elif input_string.startswith('empty'):
        print(0 if stk else 1)
    elif input_string.startswith('top'):
        print(stk[len(stk) - 1] if stk else -1)

for _ in range(n):
    operate_input(input())