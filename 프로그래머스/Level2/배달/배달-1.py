def solution(N, road, K):
    INF = int(1e9) # 무한 의 10억
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 방문하지 않은 노드중에서 가장 최단 거리가 짧은 노드의 인덱스 찾기
    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1, N + 1):
            if not visited[i] and distance[i] < min_value:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        # 시작 노드 초기화
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

        # 시작 노드 제외 N - 1 노드들에 대해 반복
        for i in range(N - 1):

            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now] + j[1]

                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(1)

    answer = 0
    for i in range(1, N + 1):
        if distance[i] != INF and distance[i] <= K:
            answer += 1

    return answer



print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4