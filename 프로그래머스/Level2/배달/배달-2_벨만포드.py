def solution(N, road, K):
    INF = int(1e9) # 무한 의 10억
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for a, b, c in road:
        if graph[a][b] != INF:
            min_cost = min(graph[a][b], c)
            graph[a][b] = min_cost
            graph[b][a] = min_cost
        else:
            graph[a][b] = c
            graph[b][a] = c

    def bellman_ford(start):
        distance = [INF] * (N + 1)

        distance[start] = 0
        # N - 1 번 탐색
        for _ in range(N - 1):
            for u in range(1, N + 1):
                for v in range(1, N + 1):
                    if graph[u][v] != INF and distance[u] != INF:
                        cost = distance[u] + graph[u][v]
                        if cost < distance[v]:
                            distance[v] = cost

        # N 번째 확인하여 최단거리 갱신 밣생하면 음수 사이클 존재
        for u in range(1, N + 1):
            for v in range(1, N + 1):
                if graph[u][v] != INF and distance[u] != INF:
                    if distance[u] + graph[u][v] < distance[v]:
                        return None

        return distance
    distance = bellman_ford(1)
    return sum(i <= K for i in distance) if distance else -1



print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4