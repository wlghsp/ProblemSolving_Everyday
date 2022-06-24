import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

for i in range(len(arr)):
    q.append((i, arr[i]))
answer = 0
while q:
    id, tmp = q.popleft()
    for i, t in q:
        if t > tmp:
            q.append((id, tmp))
            tmp = -1
            break

    if tmp != -1:
        answer += 1
        if id == m:
            print(answer)
            break