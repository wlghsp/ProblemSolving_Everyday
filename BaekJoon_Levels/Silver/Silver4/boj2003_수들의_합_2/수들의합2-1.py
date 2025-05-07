
N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
total = 0
r = 0
for l in range(N):
    total += arr[l]
    if total == M: ans += 1

    while total >= M:
        total -= arr[r]
        r += 1
        if total == M: ans += 1

print(ans)