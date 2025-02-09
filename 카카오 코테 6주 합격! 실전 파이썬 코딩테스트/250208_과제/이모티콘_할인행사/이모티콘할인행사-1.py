import math


def solution(users, emoticons):
    answer = []

    # 1 할인율 중복 순열 만들기
    rate_perm = []
    def recur(picked, M):
        if len(picked) == M:
            rate_perm.append(picked)
            return

        for rate in [10, 20, 30, 40]:
            recur(picked + [rate], M)

    recur([], len(emoticons))

    # 2. 중복 순열 별로 계산하여 결과 담기
    for perm in rate_perm:
        total_cost = 0 # 전체 매출액
        join_cnt = 0  # 가입자 수
        for user in users:
            cost = 0
            for i in range(len(emoticons)):
                if user[0] <= perm[i]:
                    cost += emoticons[i] * (1 - perm[i] / 100)

            if cost >= user[1]:
                join_cnt += 1
            else:
                total_cost += math.floor(cost)

        answer.append([join_cnt, total_cost])

    # 3. 결과를 가입자 수 asc, 매출액 asc 정렬 후 마지막 원소 반납
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]


print(solution(
    [[40, 10000], [25, 10000]],
    [7000, 9000]
))  # [1, 5400]
