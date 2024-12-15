import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    now = list(zip(*grid)) # 행열 바꾸기
    cnt = 0
    for j in range(n):
        for i in range(m):
            if now[j][i] == 1:
                cnt += now[j][i + 1:].count(0)
    print(cnt)
