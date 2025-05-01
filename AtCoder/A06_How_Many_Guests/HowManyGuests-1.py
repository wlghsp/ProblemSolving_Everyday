
N, Q = map(int, input().split())
visitors = [0] + list((map(int, input().split())))
pre_sum = [0] * (N + 1)
for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i - 1] + visitors[i]

for _ in range(Q):
    a, b = map(int, input().split())
    print(pre_sum[b] - pre_sum[a - 1])