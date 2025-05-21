import sys

input = sys.stdin.readline
N, M = map(int, input().split())

visited = [False] * (N + 1)

graph = {i: [] for i in range(N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True

    for j in graph[x]:
        if visited[j]: continue
        dfs(j)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)