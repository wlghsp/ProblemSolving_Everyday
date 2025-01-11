from collections import deque

# 인접 리스트 (in 딕셔너리)
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D', 'E'},
    'D': {'B', 'C', 'E'},
    'E': {'C', 'D', 'F'},
    'F': {'E'}
}

# BFS 구현

q = deque(['A'])
seen = {'A'}

while q:
    curr = q.popleft()

    print(curr)

    for node in graph[curr]:
        if node in seen:
            continue
        seen.add(node)
        q.append(node)
