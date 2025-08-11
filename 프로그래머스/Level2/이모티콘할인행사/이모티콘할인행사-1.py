import math


def solution(users, emoticons):
    answer = (0, 0)

    def calc(rates):
        nonlocal answer
        join_cnt = 0
        total_sale = 0
        for user_rate, user_price in users:
            cost = 0
            for rate, emoticon in zip(rates, emoticons):
                if rate >= user_rate:
                    cost += emoticon * ((100 - rate) / 100)
            total_sale += cost

            if cost >= user_price:
                join_cnt += 1
                total_sale -= cost

        cur = (join_cnt, math.trunc(total_sale))
        if cur > answer:
            answer = cur

    def recur(picked, M):
        if len(picked) == M:
            calc(picked)
            return
        for rate in [10, 20, 30, 40]:
            recur(picked + [rate], M)

    recur([], len(emoticons))

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]