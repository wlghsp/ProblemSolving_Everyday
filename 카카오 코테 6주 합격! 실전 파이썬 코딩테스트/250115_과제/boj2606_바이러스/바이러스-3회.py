

N = int(input())
pair_cnt = int(input())
tree = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)

for _ in range(pair_cnt):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for node in tree[v]:
        if not visited[node]:
            cnt += 1
            dfs(node)

dfs(1)
print(cnt)
