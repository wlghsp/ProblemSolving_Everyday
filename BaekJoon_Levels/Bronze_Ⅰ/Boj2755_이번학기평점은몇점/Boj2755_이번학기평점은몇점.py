import sys, decimal

input = lambda: sys.stdin.readline().rstrip()

grade_table = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
               'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
               'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
               'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
               'F': 0.0}

# 1. 과목 수 N
N = int(input())

# 2. 각 과목의 과목명, 학점, 성적

sum_credits = 0
scores = 0.0
for _ in range(N):
    subject, credit, score = input().split()
    credit = float(credit)
    score = grade_table[score]
    scores += credit * score
    sum_credits += credit

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

# 연산 결과를 정확한 소수점으로 받기 위해 미리 Decimal을 씀
result = decimal.Decimal(scores) / decimal.Decimal(sum_credits)

print("{:.2f}".format(result))
