from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
answer = []
while q:
    node = q.popleft()
    answer.append(node)

    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)


print(*answer, sep=' ')