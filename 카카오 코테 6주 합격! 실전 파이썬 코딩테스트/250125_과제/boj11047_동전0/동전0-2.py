
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
'''
1. 명제: 가장 큰 동전부터 정산하면 동전 갯수가 최소
2. 부정: 가장 크지 않은 동전부터 정산해도 동전 갯수가 최소
3. 모순:

K = 640
coins = [10, 50, 100]
10원 동전부터 사용하면 
- 10원 동전 64 개 필요
50원부터 사용하면
- 50원 12개, 10원 4개 = 16개 필요

큰 동전부터 사용하면
- 100원 6개, 10원 4개 = 10개 필요

** 부정이 모순이므로 명제는 참이다.
'''