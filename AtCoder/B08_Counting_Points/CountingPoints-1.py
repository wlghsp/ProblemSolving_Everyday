N = int(input())
A = [[0] * 1501 for _ in range(1501)]
S = [[0] * 1501 for _ in range(1501)]

for _ in range(N):
    x, y = map(int, input().split())
    A[x][y] += 1

for i in range(1, 1501):
    for j in range(1, 1501):
        S[i][j] = A[i][j] + S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    res = S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1]
    print(res)
