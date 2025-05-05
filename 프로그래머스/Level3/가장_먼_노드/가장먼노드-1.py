from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distances = [-1] * (n + 1)
    q = deque()
    q.append(1)
    distances[1] = 0
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if distances[next_node] != -1: continue

            distances[next_node] = distances[node] + 1
            q.append(next_node)

    answer = 0
    max_distance = max(distances)
    for d in distances:
        if d == max_distance:
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
