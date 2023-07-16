import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))


def strike_check(k, num):
    a = list(str(k))
    b = list(str(num))
    strike_cnt = 0
    ball_cnt = 0

    for d in range(3):
        if a[d] == b[d]:
            strike_cnt = strike_cnt + 1
        elif b[d] in a:
            ball_cnt = ball_cnt + 1
    return [strike_cnt, ball_cnt]

def different_number(number):
    num = str(number)
    return num[0] == num[1] or num[0] == num[2] or num[1] == num[2]

def zero_included(number):
    return '0' in str(number)

ans = 0

for i in range(123, 1000):
    if different_number(i):
        continue
    if zero_included(i):
        continue
    okay = True
    for line in lines:
        number, strike, ball = line[0], line[1], line[2]
        cnts = strike_check(i, number)
        if strike != cnts[0] or ball != cnts[1]:
            okay = False
    if okay:
        ans = ans + 1

print(ans)