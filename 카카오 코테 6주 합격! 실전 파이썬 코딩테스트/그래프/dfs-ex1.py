
# 인접 리스트 (in 딕셔너리)
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D', 'E'},
    'D': {'B', 'C', 'E'},
    'E': {'C', 'D', 'F'},
    'F': {'E'}
}

# DFS 구현

s = ['A']
seen = {'A'}

while s:
    cur = s.pop()

    print(cur)

    for node in graph[cur]:
        if node in seen:
            continue

        seen.add(node) # 본 것으로 기록
        s.append(node) # 방문 하도록 추가

# 그림 설명
