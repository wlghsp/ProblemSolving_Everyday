

N, M = map(int, input().split())


def recur(picked):
    if len(picked) == M:
        print(*picked, end="\n")
        return

    for i in range(1, N + 1):
        # if i in picked: continue
        # 같은 수를 여러 번 골라도 되므로 체크하지 않음

        recur(picked + [i])

recur([])