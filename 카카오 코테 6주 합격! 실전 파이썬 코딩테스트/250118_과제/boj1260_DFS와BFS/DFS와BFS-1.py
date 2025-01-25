from collections import deque

N, M, V = map(int, input().split())

tree = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1, N + 1):
    tree[i] = sorted(tree[i])

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for a in tree[v]:
        if not visited[a]:
            dfs(a)

def bfs(v):
    visited[v] = True
    print(v, end=' ')
    dq = deque([v])

    while dq:
        pv = dq.popleft()

        for p in tree[pv]:
            if not visited[p]:
                visited[p] = True
                print(p, end=' ')
                dq.append(p)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)