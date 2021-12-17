"""

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
MP = [list(input()) for _ in range(N)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def dfs(i, j):
    if MP[i][j] == "0":
        return 0
    MP[i][j] = "0"
    ret = 1
    for way in range(4):
        ii, jj = i + dx[way], j + dy[way]
        if ii < 0 or jj < 0 or ii == N or jj == N:
            continue
        ret += dfs(ii, jj)
    return ret


lst = []  # 단지수, 집 수
for i in range(N):
    for j in range(N):
        if MP[i][j] == "1":
            lst.append(dfs(i, j))  # 집의 수

print(len(lst))
print("\n".join(map(str, sorted(lst))))
