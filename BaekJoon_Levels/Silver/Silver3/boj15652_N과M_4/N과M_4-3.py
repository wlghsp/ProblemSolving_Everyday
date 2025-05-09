N, M = map(int, input().split())

def recur(picked, start):
    if len(picked) == M:
        print(*picked)
        return

    for i in range(start, N + 1):
        picked.append(i)
        recur(picked, i)
        picked.pop()



recur([], 1)