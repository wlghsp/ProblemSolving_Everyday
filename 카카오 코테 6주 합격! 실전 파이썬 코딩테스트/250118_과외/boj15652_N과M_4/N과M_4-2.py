
N, M = map(int, input().split())

def recur(picked, start):
    if len(picked) == M:
        print(*picked, end="\n")
        return

    for i in range(start, N + 1):

        recur(picked + [i], i)

recur([], 1)