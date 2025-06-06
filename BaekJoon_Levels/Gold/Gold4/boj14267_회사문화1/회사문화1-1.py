import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(N + 1)}
boss = [0] + list(map(int, input().split()))
compliments = [0] * (N + 1)

for i in range(1, N + 1):
    graph[i].append(boss[i])


def dfs(x):
    pass


for _ in range(M):
    i, w = map(int, input().split())
