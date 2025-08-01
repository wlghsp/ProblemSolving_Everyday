
N, K = map(int, input().split())

triangle = [[1] * N for _ in range(N)]
for i in range(2, N):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

print(triangle[N - 1][K - 1])