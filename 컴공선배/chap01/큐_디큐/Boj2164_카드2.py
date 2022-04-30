
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dq = deque()
for i in range(1, N+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())