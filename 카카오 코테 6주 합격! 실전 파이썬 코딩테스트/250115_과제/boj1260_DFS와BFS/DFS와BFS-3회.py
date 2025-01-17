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
    for node in tree[v]:
        if not visited[node]:
            dfs(node)


def bfs(v):
    visited[v] = True
    dq = deque([v])
    print(v, end=' ')
    while dq:
        popped = dq.popleft()

        for node in tree[popped]:
            if not visited[node]:
                visited[node] = True
                print(node, end=' ')
                dq.append(node)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)