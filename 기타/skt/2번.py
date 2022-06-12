'''
납부내역과 납부 예정 금액 분석
* 알림 대상
1. 이번달에는 VIP가 아니지만 다음 달에 VIP가 되는 고객
2. 이번달에는 VIP지만 다음 달에는 VIP가 아니게 되는 고객


periods : 고객들의 가입기간
payments: 고객들의 납부내역
estimates: 고객들의 납부 예정 금액
'''


def solution(periods, payments, estimates):
    answer = [0, 0]

    for i in range(len(periods)):
        period_thismonth = periods[i]
        period_nextmonth = periods[i] + 1
        sum_thismonth = sum(payments[i])
        sum_nextmonth = sum(payments[i][1:]) + estimates[i]
        vip_thismonth = False
        vip_nextmonth = False
        if 59 >= period_thismonth >= 24 and sum_thismonth >= 900000:
            vip_thismonth = True
        if period_thismonth >= 60 and sum_thismonth >= 600000:
            vip_thismonth = True

        if 59 >= period_nextmonth >= 24 and sum_nextmonth >= 900000:
            vip_nextmonth = True
        if period_nextmonth >= 60 and sum_nextmonth >= 600000:
            vip_nextmonth = True

        if not vip_thismonth and vip_nextmonth:
            answer[0] += 1
        if vip_thismonth and not vip_nextmonth:
            answer[1] += 1
        # print(period_thismonth, period_nextmonth, sum_thismonth, sum_nextmonth)

    return answer


print(solution([20, 23, 24],
               [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
                [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
                [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
               [100000, 100000, 100000])) # [1, 1]
print(solution([24, 59, 59, 60],
               [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
               [350000, 50000, 40000, 50000]))  # [2, 1]
