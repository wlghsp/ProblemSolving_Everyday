"""





"""

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()


N, K = map(int, input().split())

dq = deque(range(1, N + 1))

ans = list()

while len(dq):
    dq.rotate(-K + 1)
    ans.append(dq.popleft())

print(str(ans)[1:-1])
print(f"<{str(ans)[1:-1]}>")
