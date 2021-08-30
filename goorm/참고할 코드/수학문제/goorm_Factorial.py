"""
5

120

10

3628800

"""
import sys
input = lambda: sys.stdin.readline().rstrip()

# 3. 재귀함수 사용
# def factorial_recursive(n):
#     return n * factorial_recursive(n-1) if n > 1 else 1

# 1.  내장 팩토리얼 함수 사용 
# import math

# print(math.factorial(n))

# 2. 단순 반복문
# def factorial_for(n):
# 	ret = 1
# 	for i in range(1, n+1):
# 		ret *= i
# 	return ret

# print(factorial_for(n))

#  4.reduce 사용
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

n = int(input())

print(factorial_reduce(n))
