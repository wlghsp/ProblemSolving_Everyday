N, M = map(int, input().split())


def recur(picked, start):
    if len(picked) == M:
        print(*picked, end='\n')
        return

    for i in range(start, N + 1):
        recur(picked + [i], i) # start를 i로 설정 중복 허용

recur([], 1)