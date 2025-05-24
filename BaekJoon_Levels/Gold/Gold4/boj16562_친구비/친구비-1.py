import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
min_cost = 0
visited = [False] * (N + 1)
graph = {i: set() for i in range(N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def dfs(x, group):
    visited[x] = True

    for j in graph[x]:
        if not visited[j]:
            group.append(j)
            dfs(j, group)

for i in range(1, N + 1):
    if not visited[i]:
        group = [i]
        dfs(i, group)
        if group:
            min_cost += min(A[k] for k in group)

print(min_cost if min_cost <= K else "Oh no")