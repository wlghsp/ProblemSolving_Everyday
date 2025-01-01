
N, M = map(int, input().split())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
b = []
for i in range(N):
    b.append(list(map(int, input().split())))
    for j in range(M):
        print(a[i][j] + b[i][j], end=' ')
    print()

