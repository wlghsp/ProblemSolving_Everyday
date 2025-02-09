import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
cnt = 0

def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)