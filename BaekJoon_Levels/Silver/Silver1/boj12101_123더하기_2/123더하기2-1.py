N, K = map(int, input().split())

ans = []
def recur(picked):
    if len(picked) > 10:
        return

    if sum(picked) == N:
        ans.append(picked[:])
        return

    for i in range(1, 4):
        picked.append(i)
        recur(picked)
        picked.pop()

recur([])

if len(ans) < K:
    print(-1)
else:
    print(*ans[K - 1], sep='+')
