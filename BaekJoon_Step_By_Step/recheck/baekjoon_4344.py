import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    case = list(map(int, input().split()))
    average = sum(case[1:]) / case[0]
    cnt = 0
    for i in case[1:]:
        if i > average:
            cnt += 1
    print(str('%.3f' % round(cnt/case[0]*100, 3)) + '%')
    # 소수점 반올림해서 세번째자리까지 표시
