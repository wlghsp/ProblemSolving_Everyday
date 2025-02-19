N = int(input())
chars = input()

b_cnt = 0
r_cnt = 0
prev = chars[0]
if prev == 'B':
    b_cnt += 1
else:
    r_cnt += 1

for c in chars:
    if prev != c:
        if prev == 'B':
            b_cnt += 1
        else:
            r_cnt += 1
        prev = c

print(min(b_cnt, r_cnt) + 1)

