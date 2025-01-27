import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 찾기 연산 (같은 집합에 속하는지 확인하기 위한 함수)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0: # union
        union(a, b)
    elif q == 1: # find
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
