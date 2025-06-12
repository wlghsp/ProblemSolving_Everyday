import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(N + 1)}
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = True

    for nx in graph[x]:
        if visited[nx]: continue

        dfs(nx)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)