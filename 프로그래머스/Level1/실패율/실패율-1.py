def solution(N, stages):
    fail_rates = []
    for i in range(1, N + 1):
        total = 0
        not_clear = 0
        for s in stages:
            if s >= i:
                total += 1
                if s == i:
                    not_clear += 1
        # division by zero 가 발생할 수 있으므로 나눗셈에는 분모가 0인 경우 체크
        fail_rates.append((i, not_clear / total if total != 0 else 0))
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    return list(map(lambda x: x[0], fail_rates))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]