N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
reachable = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        reachable[i][j] = True if adj[i][j] else False

for k in range(N):
    for i in range(N):
        for j in range(N):
            reachable[i][j] = reachable[i][j] or (reachable[i][k] == 1 and reachable[k][j] == 1)

result = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1 if reachable[i][j] else 0)
    result.append(row)

for row in result:
    print(*row, sep=' ')