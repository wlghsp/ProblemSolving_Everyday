INF = int(1e9)
n = 4 # 노드 개수
dist = [[INF] * n for _ in range(n)]

# 자기 자신으로 가는 경로는 0으로 초기화
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
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
# 결과 출력
for row in dist:
    print(row)