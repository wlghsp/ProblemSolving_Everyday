import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque



N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N + 1) # 거리와 방문을 동시에 체크함. -1이면 방문하지 않은 상태

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(Node):
    answer = []
    dq = deque()
    dq.append(Node)

    visited[Node] += 1

    while dq:
        now_node = dq.popleft()
        for i in graph[now_node]:
            if visited[i] == -1:
                # 방문할 때마다 거리를 늘려준다.
                visited[i] = visited[now_node] + 1 # 이전 노드의 방문 노드 거리 + 1
                dq.append(i)

    for i in range(N+1):
        if visited[i] == K:
            answer.append(i)

    if len(answer) == 0:
        print("-1")
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(X)