import sys

sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N, A, B = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

visited = [False] * (N + 1)
ans = float('inf')

def dfs(curr, target, total, max_dist):
    global ans
    visited[curr] = True

    if curr == target:
        ans = min(ans, total - max_dist)
        return

    for next, d in graph[curr]:
        if visited[next]: continue

        dfs(next, target, total + d, max(max_dist, d))

dfs(A, B, 0, 0)
print(ans)
