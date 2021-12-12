"""
a x사의 1리터당 요금
b y사의 기본요금
c y사의 요금이 기본요금이 되는 사용량의 상한
d y사의 1리터랑 
p JOI군의 집에서 사용하는 한 달간 수도의 양 P

9
100
20
3
10

90

8
300
100
10
250

1800

"""
import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

option_x = p * a

if c >= p:
    option_y = b
else:
    option_y = b + (p - c) * d

print(min((option_x, option_y)))
