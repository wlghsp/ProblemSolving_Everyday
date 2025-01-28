import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [-1] * (N + 1)

def dfs(v):
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            parents[node] = v
            dfs(node)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])