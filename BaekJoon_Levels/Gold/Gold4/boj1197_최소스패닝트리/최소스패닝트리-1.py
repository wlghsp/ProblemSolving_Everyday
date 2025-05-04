import sys

sys.setrecursionlimit(10 ** 6)
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parent = [i for i in range(V + 1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb

def kruskal():
    edges.sort(key=lambda x: x[2])

    total = 0

    for a, b, cost in edges:
        if find(a) != find(b):
            union(a, b)
            total += cost

    return total

print(kruskal())