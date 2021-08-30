"""
5 6 8

14.98


5 7 9

17.41

문제에서 힌트를 줘서 너무 쉽게 풀었음 . 

힌트: 헤론의 공식 

s = (a+b+c)/2

삼각형의 넓이 = (s*(s-a)*(s-b)*(s-c))**(0.5)

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

nums = list(map(int, input().split()))

a = nums[0]
b = nums[1]
c = nums[2]

s = (a + b + c) / 2

result = (s * (s - a) * (s - b) * (s - c)) ** (0.5)

# print("{:.2f}".format(result))

# f string 소수점 표현
print(f"{result:.2f}")
