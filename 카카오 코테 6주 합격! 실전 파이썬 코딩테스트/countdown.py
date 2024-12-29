def countdown(n):

    # 종료 조건
    if n == 1:
        return "1 end"

    # 재귀 호출 "재귀 데이터를 받음
    recur_out = countdown(n - 1)

    cur_out = str(n)

    comb_out = cur_out + ', ' + recur_out

    return comb_out

print(countdown(5))