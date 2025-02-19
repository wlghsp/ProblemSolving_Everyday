N = int(input())
lost = list(map(int, input().split()))
lost.sort()
ans = -1
if N % 2 == 0:
    l, r = 0, len(lost) - 1
    while l < r:
        total = lost[l] + lost[r]
        ans = max(ans, total)
        l += 1
        r -= 1
    print(ans)
else:
    l, r = 0, len(lost) - 2
    while l < r:
        total = lost[l] + lost[r]
        ans = max(ans, total)
        l += 1
        r -= 1
    ans = max(ans, lost[N - 1])
    print(ans)