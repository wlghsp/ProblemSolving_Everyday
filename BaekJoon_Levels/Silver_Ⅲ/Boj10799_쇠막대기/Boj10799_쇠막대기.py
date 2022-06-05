
import sys
input = lambda : sys.stdin.readline().rstrip()

galho = input()

stk = []
answer = 0
for i in range(len(galho)):
    if galho[i] == '(':
        stk.append(galho[i])
    else:
        stk.pop()
        if galho[i-1] == '(':
            answer += len(stk)
        else:
            answer += 1

print(answer)

