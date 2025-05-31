import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    distance = [-1] * (N + 1)
    q = deque([start])
    distance[start] = 0


    while q:
        x = q.popleft()

        for nx in graph[x]:
            if distance[nx] != -1: continue

            distance[nx] = distance[x] + 1
            q.append(nx)

    return sum(distance)

min_dist = float('inf')
min_idx = 0

for i in range(1, N + 1):
    res = bfs(i)
    if min_dist > res:
        min_dist = res
        min_idx = i

print(min_idx)