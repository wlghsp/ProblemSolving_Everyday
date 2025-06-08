from collections import defaultdict

A, B, C = map(int, input().split())
graph = defaultdict(set)
for i in range(1, 11):
    for j in range(1, 11):
        if (A * i + B * j) == C:
            graph[i].add(j)

for i in range(1, 11):
    if graph[i]:
        print(*graph[i])
    else:
        print(0)