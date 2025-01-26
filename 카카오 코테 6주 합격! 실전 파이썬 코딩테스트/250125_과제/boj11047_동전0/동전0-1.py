N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0
for c in coins:
    if K >= c:
        cnt += K // c
        K = K % c


print(cnt)
