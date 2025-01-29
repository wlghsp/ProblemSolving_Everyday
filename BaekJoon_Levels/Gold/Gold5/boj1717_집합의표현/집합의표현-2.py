import sys
sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())

# 처음에는 모든 노드가 자기 자신을 부모로 가짐
# 유니온 연산을 수행하지 않았을 때, 각 노드는 독립된 집합을 이루고 있음
parents = [i for i in range(N + 1)]

def union(a, b):
    pa = find(a)
    pb = find(b)
    parents[pa] = pb

def find(x):
    if parents[x] != x: # 본인이 루트가 아니라면
        # 경로 압축: 부모를 루트 노드로 갱신
        parents[x] = find(parents[x])
    return parents[x] # 최종적으로 루트 노드 반환

for _ in range(M):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    elif q == 1:
        print("YES" if find(a) == find(b) else "NO")