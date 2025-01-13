from collections import deque

n, m, v = map(int, input().split())

visited = [False] * (n + 1)
tree = {i : [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1, n + 1):
    tree[i] = sorted(tree[i])

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for node in tree[v]:
        if not visited[node]:
            dfs(node)

def bfs(v):
    visited[v] = True
    print(v, end=' ')
    dq = deque([v])

    while dq:
        popped = dq.popleft()
        for node in tree[popped]:
            if not visited[node]:
                print(node, end=' ')
                visited[node] = True
                dq.append(node)

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)