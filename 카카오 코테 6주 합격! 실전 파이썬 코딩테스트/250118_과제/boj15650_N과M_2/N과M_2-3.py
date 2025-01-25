

N, M = map(int, input().split())

def recur(picked, start):
    if len(picked) == M:
        print(*picked, end='\n')
        return


    for i in range(start, N + 1):
        if i in picked: continue

        recur(picked + [i], i + 1)

recur([], 1)