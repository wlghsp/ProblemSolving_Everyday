
N, M = map(int, input().split())

def recur(picked):
    if len(picked) == M:
        print(*picked, end="\n")
        return

    for i in range(1, N + 1):
        recur(picked + [i])


recur([])