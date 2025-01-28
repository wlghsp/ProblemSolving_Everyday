# 하루마다 K만큼 중량 감소
# 키트 순열을 만들어서 매번 시도하고 카운트
N, K = map(int, input().split())
exercise_kits = list(map(int, input().split()))
WEIGHT_LIMIT = 500

case_cnt = 0

def can_maintain_weight(indexes):
    can_maintain = True
    weight = 500
    for i in range(N):
        weight -= K
        weight += exercise_kits[indexes[i]]
        if weight < WEIGHT_LIMIT:
            return False

    return can_maintain

def recur(picked):
    global case_cnt
    if len(picked) == N:
        case_cnt += can_maintain_weight(picked)
        return

    for i in range(N):
        if i in picked: continue

        recur(picked + [i])

recur([])

print(case_cnt)
