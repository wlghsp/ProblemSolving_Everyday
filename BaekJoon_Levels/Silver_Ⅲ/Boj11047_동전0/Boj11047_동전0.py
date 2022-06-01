
import sys
input = lambda : sys.stdin.readline().rstrip()
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
cnt = 0
for i in range(len(coins)-1, -1, -1):
    coin = coins[i]
    if K >= coin:
        cnt += K // coin
        K %= coin
print(cnt)


