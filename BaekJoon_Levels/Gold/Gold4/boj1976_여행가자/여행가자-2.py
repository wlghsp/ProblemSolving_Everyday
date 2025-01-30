
N = int(input()) # 전체 도시의 수
M = int(input()) # 여행 계획 도시 수
connection_info = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))
parents = [i for i in range(N + 1)]

def union(a, b):
    pa = find(a)
    pb = find(b)
    parents[pa] = pb

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

for i in range(N):
    for j in range(N):
        if connection_info[i][j] == 1:
            union(i + 1, j + 1)

prev = find(travel_plan[0])
travel_possible = True
for i in range(1, M):
    if find(travel_plan[i]) != prev:
        travel_possible = False
        break

print("YES" if travel_possible else "NO")


