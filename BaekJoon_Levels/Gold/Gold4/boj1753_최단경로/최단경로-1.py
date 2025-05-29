import heapq
import sys

input = lambda : sys.stdin.readline().rstrip()
V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(V + 1)}
INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v, d in graph[now]:
            cost = dist + d
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (distance[v], v))
dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])