import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N, R, Q = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

size = [0] * (N + 1)
visited = [False] * (N + 1)
def dfs(x):
    visited[x] = True
    size[x] = 1

    for nx in graph[x]:
        if visited[nx]: continue
        size[x] += dfs(nx)

    return size[x]

dfs(R)

for _ in range(Q):
    print(size[int(input())])