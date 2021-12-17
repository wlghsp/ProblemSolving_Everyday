'''

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2


0 2 3 1 2 4

'''
import sys
import heapq

INF = int(1e9)
input = lambda: sys.stdin.readline().rstrip()

# 노드의 개수, 간선의 개수 
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 간선 입력
for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b 간선의 비용 : c
    graph[a].append((b,c))


def dijkstra(start):
    # 큐를 설정하여 시작점을 큐에 넣는다.
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0


    # 큐가 빌때까지 반복하여 실시한다. 
    while q:
        # 최단거리, 해당 노드를 가져온다. 
        dist, now = heapq.heappop(q)

        # 이미 처리된 값인 경우 무시한다
        if distance[now] < dist:
            continue
        
        # 인접한 노드 개수만큼 반복한다. 
        for i in graph[now]:
            cost = dist + i[1] #i[0] : 노드값, i[1] : 간선비용

            # 갱신값이 작은 경우 갱신한다. 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
