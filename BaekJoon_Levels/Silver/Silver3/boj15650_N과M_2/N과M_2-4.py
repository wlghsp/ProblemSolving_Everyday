
N, M = map(int, input().split())

def recur(picked, start):
    if len(picked) == M:
        print(*picked, sep=' ')
        return
    for i in range(start, N + 1): # start 부터 시작하므로 오름차순 보장
        picked.append(i)
        recur(picked, i + 1)
        picked.pop()

recur([], 1)