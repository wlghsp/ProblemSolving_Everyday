


import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N = int(input())

dq = deque()
for i in range(1, N+1):
    dq.append(i)


while dq:
    print(dq.popleft(), end=' ')
    if not dq:
        break
    dq.append(dq.popleft())

