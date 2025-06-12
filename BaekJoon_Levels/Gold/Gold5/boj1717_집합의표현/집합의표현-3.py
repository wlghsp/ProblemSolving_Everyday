import sys

sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    pa = find(a)
    pb = find(b)
    parents[pa] = pb


for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    elif c == 1:
        print("YES" if find(a) == find(b) else "NO")
