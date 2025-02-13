import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
dist = [-1] * (N + 1) # 방문처리에도 사용을 위해 처음부터 -1로 초기화
graph = [[] for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    dist[start] = 0 # start 방문했으므로 0으로 초기화
    q = deque([start])

    while q:
        x = q.popleft()

        for node in graph[x]:
            if dist[node] != -1: continue # -1 이 아니면 방문한 경우

            dist[node] = dist[x] + 1
            q.append(node)

bfs(X)

answer = [i for i, d in enumerate(dist) if d == K]
if answer:
    # print(*answer, sep='\n')
    print('\n'.join(map(str, answer)))
else:
    print(-1)
