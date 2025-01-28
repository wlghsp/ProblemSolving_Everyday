
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

result = []

while q:
    v = q.popleft()
    result.append(v)
    for node in graph[v]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            q.append(node)

print(*result)