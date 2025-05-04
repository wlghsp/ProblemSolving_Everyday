import heapq


def solution(N, road, K):
    INF = int(1e9) # 무한 의 10억
    distance = [INF] * (N + 1)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for a, b, c in road:
        if graph[a][b] != INF:
            min_cost = min(graph[a][b], c)
            graph[a][b] = min_cost
            graph[b][a] = min_cost
        else:
            graph[a][b] = c
            graph[b][a] = c

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            # 같은 노드가 여러 번 큐에 들어 갈 수 있음
            # 이미 더 짧은 길로 갔던 애는 무시
            # 느린 경로 중복 방문 안전 장치
            if distance[now] < dist: continue

            for i in range(1, N + 1):
                cost = graph[now][i] + dist
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    dijkstra(1)
    return sum(i <= K for i in distance)



print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4