import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    W = int(input())
    q = deque()
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = build_time[i]

    while q:
        now = q.popleft()

        for neighbor in graph[now]:
            in_degree[neighbor] -= 1
            dp[neighbor] = max(dp[now] + build_time[neighbor], dp[neighbor])
            if in_degree[neighbor] == 0:
                q.append(neighbor)

        if now == W:
            break
    print(dp[W])