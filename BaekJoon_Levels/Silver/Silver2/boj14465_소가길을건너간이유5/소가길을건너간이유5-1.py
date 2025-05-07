
N, K, B = map(int, input().split())
broken = [int(input()) for _ in range(B)]
crosswalks = [False] * (N + 1)

for b in broken:
    crosswalks[b] = True

total = sum(crosswalks[1:K + 1])
ans = float('inf')
for i in range(K + 1, N + 1):
    total = total - crosswalks[i - K] + crosswalks[i]
    ans = min(ans, total)

print(ans)
