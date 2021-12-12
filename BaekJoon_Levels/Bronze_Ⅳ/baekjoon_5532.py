"""
l 방학일수
a 국어숙제
b 수학숙제
c 하루 상근 국어 가능 페이지 
d 하루 상근 수학 가능 페이지 
"""
import sys, math

input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# literatureDays = (a // c) + 1 if a % c != 0 else (a // c)
# mathDays = (b // d) + 1 if a % c != 0 else (b // d)

# no_homework_days = l - literatureDays if literatureDays >= mathDays else l - mathDays

# print(no_homework_days)

print(l - max(math.ceil(a / c), math.ceil(b / d)))
