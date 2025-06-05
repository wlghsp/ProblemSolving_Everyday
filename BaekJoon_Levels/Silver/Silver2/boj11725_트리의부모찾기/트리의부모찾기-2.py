import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
parents = [-1] * (N + 1)
visited = [False] * (N + 1)
graph = {i: []  for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if visited[nx]: continue

        parents[nx] = x
        dfs(nx)
dfs(1)

print(*parents[2:], sep='\n')