
from collections import deque


dq = deque()

dq.append(123)
dq.append(456)
dq.append(789)

while len(dq):
    print(dq.popleft())
