import sys
input = lambda : sys.stdin.readline().rstrip()

dy = [[0] * 101 for _ in range(101)]



def DFS(n, m):
    if dy[n][m] != 0: return dy[n][m]
    if n == m or m == 0: return 1
    else:
        dy[n][m] = DFS(n - 1, m - 1) + DFS(n - 1, m)
        return dy[n][m]


n, m = map(int, input().split())
print(DFS(n, m))




