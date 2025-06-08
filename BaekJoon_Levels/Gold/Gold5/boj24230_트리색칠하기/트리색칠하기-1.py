import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
colors = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (N + 1)

# dfs에서는 자식만 색깔이 확인 되므로 미리 루트도 칠해야 하는지 확인
if colors[1] != 0:
    cnt += 1

def dfs(parent):
    global cnt
    visited[parent] = True

    for child in graph[parent]:
        if visited[child]: continue

        if colors[parent] != colors[child]:
            cnt += 1
        dfs(child)

dfs(1)
print(cnt)