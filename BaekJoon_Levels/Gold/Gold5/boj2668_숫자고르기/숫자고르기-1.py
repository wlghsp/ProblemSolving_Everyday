import sys

sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [0] + [int(input()) for _ in range(N)]

res = []
def dfs(start, curr, path, visited):
    visited[curr] = True
    path.append(curr)

    next_node = nums[curr]
    if not visited[next_node]:
        dfs(start, next_node, path, visited)
    elif next_node == start:
        res.extend(path)


for i in range(1, N + 1):
    visited = [False] * (N + 1)
    path = []
    dfs(i, i, path, visited)

res = sorted(set(res))
print(len(res))
print(*res, sep='\n')

