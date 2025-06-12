import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
boss = [0] + list(map(int, input().split()))
compliments = [0] * (N + 1)
graph = {i: [] for i in range(1, N + 1)}

for i in range(2, N + 1):
    graph[boss[i]].append(i)

for _ in range(M):
    i, w = map(int, input().split())
    compliments[i] += w


def dfs(x):
    for nx in graph[x]:
        compliments[nx] += compliments[x]
        dfs(nx)


dfs(1)
print(*compliments[1:], sep=' ')
