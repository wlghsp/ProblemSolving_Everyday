
import sys
input = lambda : sys.stdin.readline().rstrip()

galho = input()

stk = []
answer = 0
for i in range(len(galho)):
    if galho[i] == '(':
        stk.append(galho[i])
    else:
        if galho[i-1] == '(':
            stk.pop()
            answer += len(stk)
        else:
            stk.pop()
            answer += 1

print(answer)

