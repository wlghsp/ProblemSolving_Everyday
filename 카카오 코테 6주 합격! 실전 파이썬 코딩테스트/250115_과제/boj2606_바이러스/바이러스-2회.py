
N = int(input())
pair_cnt = int(input())
visited = [False] * (N + 1)
tree = {i : [] for i in range(1, N + 1)}

result = 0

for _ in range(pair_cnt):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    global result
    visited[v] = True

    for node in tree[v]:
        if not visited[node]:
            result += 1
            dfs(node)

dfs(1)

print(result)