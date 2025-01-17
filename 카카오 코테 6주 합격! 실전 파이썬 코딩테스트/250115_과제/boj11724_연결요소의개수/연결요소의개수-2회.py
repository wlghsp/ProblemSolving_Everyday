import sys

sys.setrecursionlimit(10 ** 6)

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
visited = [False] * (N + 1)
tree = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(v):
    visited[v] = True

    for node in tree[v]:
        if not visited[node]:
            dfs(node)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)