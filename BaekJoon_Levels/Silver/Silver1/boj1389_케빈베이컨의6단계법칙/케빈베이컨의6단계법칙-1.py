from collections import deque

N, M = map(int, input().split())
people = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, visited):
    visited[start] = True
    q = deque([start])
    cnt = 0
    while q:
        pv = q.popleft()
        for node in graph[pv]:
            if visited[node] != -1: continue

            visited[node] = visited[pv] + 1
            q.append(node)
    return sum(visited)

min_dist = float('inf')
min_person = -1
for i in range(1, N + 1):
    total = bfs(i, [-1] * (N + 1))
    if min_dist > total:
        min_dist = total
        min_person = i

print(min_person)
