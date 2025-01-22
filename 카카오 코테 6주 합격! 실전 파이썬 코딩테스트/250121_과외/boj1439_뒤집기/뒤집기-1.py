
S = input()

# zero, one 뭉치 카운트
# 적은 횟수 출력

zero_cnt = 0
one_cnt = 0

prev = S[0]
for i in range(1, len(S)):
    if prev != S[i]: # 문자가 바뀔 때 카운트
        if prev == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
        prev = S[i]

    if i == len(S) - 1: # 마지막 뭉치 처리 필요
        if prev == '0': zero_cnt += 1
        else: one_cnt += 1


print(min(zero_cnt, one_cnt))