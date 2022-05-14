
import sys

input = lambda : sys.stdin.readline().rstrip()

while 1:
    string = input()
    stack = []
    true_flag = 1

    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break

    if string == '.': # 입력의 종료 조건
        break

    print("yes" if true_flag and not(stack) else "no")