
N, M = map(int, input().split())

def recur(picked):
    if len(picked) == M:
        print(*picked, sep=' ')
        return

    for i in range(1, N + 1):
        picked.append(i)
        recur(picked)
        picked.pop()

recur([])
