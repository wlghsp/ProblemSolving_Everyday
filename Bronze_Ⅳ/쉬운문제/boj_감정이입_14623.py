"""
1010
11

11110

1000
100

100000

10진수로 변환 후 곱셈 후 2진수로 변환하여 출력 
format함수 인자 "b" 로 앞에 기호제거  
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

a = int(input(), 2)
b = int(input(), 2)

result = a * b
print(format(result, "b"))
