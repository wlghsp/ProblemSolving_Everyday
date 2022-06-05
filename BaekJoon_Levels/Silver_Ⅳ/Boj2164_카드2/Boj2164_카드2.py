



from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dq = deque()

N = int(input())

for i in range(1, N+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    card = dq.popleft()
    dq.append(card)

print(dq[0])