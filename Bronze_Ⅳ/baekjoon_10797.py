"""
10부제  
자동차번호 일의 자리 숫자와 날짜의 일의자리 숫자가 일치하면 자동차의 운행 금지 
1
1 2 3 4 5

1

3
1 2 3 5 3

2
"""
import sys

input = sys.stdin.readline

day = int(input())
car_nums = list(map(int, input().split()))

count = 0
if day in car_nums:
    for num in car_nums:
        if num == day:
            count += 1
    print(count)
else:
    print(0)
