import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())

visited = [False] * (N + 1)
tree = defaultdict(list)
parents = [1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(cur):
    visited[cur] = True

    for node in tree[cur]:
        if not visited[node]:
            parents[node] = cur
            dfs(node)


dfs(1)

for i in range(2, N + 1):
    print(parents[i])
