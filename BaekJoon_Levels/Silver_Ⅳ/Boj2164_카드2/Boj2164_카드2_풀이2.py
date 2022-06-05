



from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dq = deque()

N = int(input())

for i in range(N):
    dq.append(N-i)

while len(dq) > 1:
    dq.pop()
    dq.appendleft(dq.pop())

print(dq.popleft())