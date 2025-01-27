import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    # 건물의 번호는 1~N까지이므로 인덱스 맞추기 위해 0 추가
    in_degree = [0] * (N + 1) # 각 정점의 진입 차수
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y) # x를 지어야 y를 지을 수 있다.
        in_degree[y] += 1 # 오는 간선 진입 차수 +1

    W = int(input()) # 지어야할 건물의 번호

    time = [0] * (N + 1) # 각 건물이 건설되는 데 걸리는 시간을 저장하는 배열
    q = deque() # 위상 정렬을 위한 큐
    for i in range(1, N + 1):
        if in_degree[i] == 0: # 진입 차수가 0이면
            q.append(i)
            time[i] = build_time[i] # root이므로 건설시간 갱신

    # 위상 정렬 및 소요시간 계산
    while q:
        now = q.popleft() # 현재 건설이 완료된 건물
        for node in graph[now]: # 현재 건물 이후로 지을 수 있는 건물 탐색
            in_degree[node] -= 1 # 방문 노드 진입 차수 -1
            time[node] = max(time[node], time[now] + build_time[node])
            if in_degree[node] == 0: # 진입 차수 0이된 건물을 큐에 추가
                q.append(node)
        # 목표 건물(W)에 도달하면 더 이상 탐색할 필요 없음 (최적화 가능)
        if now == W:
            break

    # 목표 건물 W를 건설하는데 걸리는 최소 시간 출력
    print(time[W])

