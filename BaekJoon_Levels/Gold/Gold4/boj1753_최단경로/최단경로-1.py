import sys

input = lambda : sys.stdin.readline().rstrip()
V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(V + 1)}
INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
