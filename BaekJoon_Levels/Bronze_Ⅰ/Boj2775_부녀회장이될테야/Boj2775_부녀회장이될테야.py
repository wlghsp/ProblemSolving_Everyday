import sys

input = lambda: sys.stdin.readline().rstrip()

apart = [[i for i in range(1, 15)]]
for _ in range(14):
    apart.append([1] + [0] * 13)

for i in range(1, 15): # 1층부터 14층까지
    for j in range(14): # 2호부터 14호까지
        apart[i][j] = apart[i][j-1] + apart[i-1][j]


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])
