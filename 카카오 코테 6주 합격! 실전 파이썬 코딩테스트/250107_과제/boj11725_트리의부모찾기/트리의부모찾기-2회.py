import sys

from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

N = int(input())
tree = defaultdict(list)
parents = [1] * (N + 1)
visited = [False] * (N + 1)

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

print(*parents[2:], sep='\n')
