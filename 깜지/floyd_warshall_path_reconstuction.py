INF = int(1e9)

n = 4  # 노드 개수

# 거리와 경로 테이블 초기화
dist = [[INF] * n for _ in range(n)]
via = [[-1] * n for _ in range(n)]

# 자기 자신은 거리 0
for i in range(n):
    dist[i][i] = 0

# 간선 정보 입력
edges = [
    (0, 1, 5),
    (0, 3, 10),
    (1, 2, 3),
    (2, 3, 1)
]

for u, v, w in edges:
    dist[u][v] = w


# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] >  dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                via[i][j] = k # i -> j 로 가는 경로 중간에 k를 거침

def get_path(i, j):
    if via[i][j] == -1:
        return [i, j] # 직접 연결 or 초기 상태
    k = via[i][j]
    return get_path(i, k)[:-1] + get_path(k, j) # 중복 노드 제거

print("최단 경로 0 -> 3:", get_path(0, 3))