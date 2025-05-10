
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
S = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        S[i][j] = A[i - 1][j - 1] + S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    res = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1]
    print(res)
