N, K = map(int, input().split())
min_cnt = K * (K + 1) / 2
if min_cnt > N:
    print(-1)
else:
    basket = [0] * K
    pass