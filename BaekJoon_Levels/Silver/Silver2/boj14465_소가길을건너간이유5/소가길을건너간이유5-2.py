N, K, B = map(int, input().split())
crosswalks = [0] * N

for _ in range(B):
    crosswalks[int(input()) - 1] = 1

total = sum(crosswalks[:K])
min_cnt = float('inf')

for i in range(K, N):
    total += crosswalks[i] - crosswalks[i - K]
    min_cnt = min(min_cnt, total)

print(min_cnt)
