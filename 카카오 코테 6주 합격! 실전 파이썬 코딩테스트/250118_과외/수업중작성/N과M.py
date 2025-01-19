
N, M = map(int, input().split())

results = []

def rec(picked, m):
    if m == M:
        results.append(picked)
        return

    for i in range(1, N + 1):
        if i in picked: continue

        rec(picked + [i], m + 1)


rec([], 0)

for result in results:
    print(*result)