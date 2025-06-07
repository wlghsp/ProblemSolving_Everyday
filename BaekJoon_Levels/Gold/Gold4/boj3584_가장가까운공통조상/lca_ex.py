

N = 7
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1) # 각 노드의 부모 저장
depth = [0] * (N + 1) # 각 노드의 깊이 저장
visited = [False] * (N + 1)

def dfs(node, d):
    visited[node] = True
    depth[node] = d

    for nxt in graph[node]:
        if visited[node]: continue

        parent[nxt] = node # nxt 의 부모는 node
        dfs(nxt, d + 1)

def lca(a, b):
    # 1. 깊이를 맞춘다.
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]

    # 2. 공통 조상을 찾는다
    while a != b:
        a = parent[a]
        b = parent[b]
    return a



