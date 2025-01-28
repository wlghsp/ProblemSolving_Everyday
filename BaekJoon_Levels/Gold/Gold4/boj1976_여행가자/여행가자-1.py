import sys

input = lambda: sys.stdin.readline().rstrip()

# 유니온 파인드
N = int(input())
M = int(input())
connection_info = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split())) # 여행 계획
parent = [i for i in range(N + 1)]

# 부모 노드 찾기 (경로 압축 사용)
def find(x):
    if  parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 노드를 같은 집합으로 묶기
def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb

# 같은 집합으로 묶기
# 대칭 행렬이므로 중복된 탐색을 없애기 위해 i + 1 부터 탐색
# 연산횟수 절반으로 줄어듬
for i in range(N):
    for j in range(i + 1, N):
        if connection_info[i][j] == 1:
            union(i + 1, j + 1)

# 여행계획이 모두 같은 집합에 있다면 여행 가능
is_same_group = True
for i in range(len(travel_plan) - 1):
    if find(travel_plan[i]) != find(travel_plan[i + 1]):
        # 서로 다른 그룹을 발견하는 즉시 NO 출력 후 종료
        print("NO")
        exit()
print("YES")