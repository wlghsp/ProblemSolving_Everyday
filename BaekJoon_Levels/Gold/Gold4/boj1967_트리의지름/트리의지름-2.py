import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    p, s, w = map(int, input().split())
    graph[p].append((s, w))
    graph[s].append((p, w))
visited = [-1] * (N + 1)

def dfs(x, total):
    visited[x] = total

    for nx, weight in graph[x]:
        if visited[nx] != -1:
            continue
        dfs(nx, total + weight)


dfs(1, 0)
max_weight = max(visited)
max_node = 0
for i in range(1, N + 1):
    if max_weight == visited[i]:
        max_node = i

visited = [-1] * (N + 1)
dfs(max_node, 0)

print(max(visited))