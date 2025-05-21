import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = {i: [] for i in range(N + 1)}
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = -1
visited = [False] * (N + 1)
def dfs(x, cnt):
    global ans
    visited[x] = True

    if x == b:
        ans = cnt
        return

    for j in graph[x]:
        if visited[j]: continue

        dfs(j, cnt + 1)


dfs(a, 0)
print(ans)