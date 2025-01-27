
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0
for coin in coins:
    if K >= coin:
        cnt += K // coin
        K %= coin
    if K <= 0:
        break
print(cnt)
