import math


def solution(users, emoticons):
    len_emo = len(emoticons)
    best_result = (0, 0)

    def recur(picked): # 중복 순열
        nonlocal best_result

        if len(picked) == len_emo:
            join_cnt, total_cost = 0, 0
            for rate, price in users:
                user_total = 0
                for item_price, item_rate in zip(emoticons, picked):
                    if item_rate >= rate:
                        user_total += item_price * (1 - item_rate / 100)
                if user_total >= price:
                    join_cnt += 1
                else:
                    total_cost += math.floor(user_total)
            best_result = max(best_result, (join_cnt, total_cost))
            return

        for rate in [10, 20, 30, 40]:
            recur(picked + [rate])

    recur([])

    return best_result


print(solution(
    [[40, 10000], [25, 10000]],
    [7000, 9000]
))  # [1, 5400]
