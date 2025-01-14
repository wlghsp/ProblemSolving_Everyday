from collections import defaultdict, deque

N, M, V = map(int, input().split())
visited = [False] * (N + 1)

tree = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(1, N + 1):
    tree[i] = sorted(tree[i])

def dfs(x, visited):
    visited[x] = True
    print(x, end=' ')
    for node in tree[x]:
        if not visited[node]:
            dfs(node, visited)


def bfs(x, visited):
    print(x, end=' ')
    visited[x] = True

    dq = deque([x])

    while dq:
        popped = dq.popleft()

        for node in tree[popped]:
            if not visited[node]:
                visited[node] = True
                print(node, end=' ')
                dq.append(node)

dfs(V, visited)
print()
visited = [False] * (N + 1)
bfs(V, visited)
