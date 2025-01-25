S = input()

zero_cnt = 0
one_cnt = 0

prev = S[0]
for i in range(1, len(S)):
    if prev != S[i]:
        if S[i] == '1':
            zero_cnt += 1
        else: one_cnt += 1

        prev = S[i]

    if len(S) - 1 == i:
        if S[i] == '1': one_cnt += 1
        else: zero_cnt += 1

print(min(zero_cnt, one_cnt))
