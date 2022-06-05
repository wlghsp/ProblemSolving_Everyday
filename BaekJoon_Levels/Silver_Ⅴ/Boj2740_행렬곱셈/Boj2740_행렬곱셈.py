
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
b = []

M, K = map(int, input().split())
for _ in range(M):
    b.append(list(map(int, input().split())))


for i in range(N):
    for j in range(K):
        sum = 0
        for k in range(M):
            sum += a[i][k] * b[k][j]
        print(sum, end=' ')
    print()


