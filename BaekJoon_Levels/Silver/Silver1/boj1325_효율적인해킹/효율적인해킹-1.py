import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cnt_arr = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

visited = [False] * (N + 1)
def bfs(x):
    cnt = 0
    visited[x] = True
    q = deque([x])
    while q:
        px = q.popleft()
        for nxt in graph[px]:
            if visited[nxt]: continue

            cnt += 1
            visited[nxt] = True
            q.append(nxt)
    return cnt

for i in range(1, N + 1):
    cnt_arr[i] = bfs(i)
    visited = [False] * (N + 1)

max_val = max(cnt_arr)
for i in range(1, N + 1):
    if max_val == cnt_arr[i]:
        print(i, end=' ')