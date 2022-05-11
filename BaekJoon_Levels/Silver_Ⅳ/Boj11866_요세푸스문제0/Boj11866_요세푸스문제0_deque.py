
# 디큐로 풀기
import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

N, K = map(int, input().split())

dq = deque()

for i in range(N):
    dq.append(i+1)

print("<", end="")

while len(dq) > 1:
    # K-1번 앞에 있는 원소를 뒤로 보낸다.
    for i in range(K-1):
        val = dq.popleft()
        dq.append(val)

    print(dq.popleft(), end=", ")

print(dq.pop(), end=">")
