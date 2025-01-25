
n, m = map(int, input().split())


answers = []
def recur(start, picked):
    if len(picked) == m:
        answers.append(picked)
        return

    # 중복 방지와 오름차순 적용 방법: 시작값 관리
    # 현재 숫자보다 작은 값을 선택하지 않도록 함
    for i in range(start, n + 1):
        if i in picked: continue

        recur(i + 1, picked + [i])


recur(1, [])
for answer in answers:
    print(*answer, sep=' ')
