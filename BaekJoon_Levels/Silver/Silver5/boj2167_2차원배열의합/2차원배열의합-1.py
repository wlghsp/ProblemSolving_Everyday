N, M = map(int, input().split())
nums = [[0] * (M + 1)]
nums += [[0] + list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + nums[i][j]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = prefix_sum[x][y] + prefix_sum[i - 1][j - 1] - prefix_sum[x][j - 1] - prefix_sum[i - 1][y]
    print(result)