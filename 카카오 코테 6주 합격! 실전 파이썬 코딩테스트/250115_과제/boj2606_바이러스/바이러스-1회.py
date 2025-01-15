
N = int(input())
visited = [False] * (N + 1)
pair_cnt = int(input())

tree = {i: [] for i in range(N + 1)}
for _ in range(pair_cnt):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for i in tree[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)

print(cnt)