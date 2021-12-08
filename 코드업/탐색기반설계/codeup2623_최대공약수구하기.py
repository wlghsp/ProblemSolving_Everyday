
"""
두 정수 a, b를 입력받아서, a, b의 최대공약수를 출력하시오.

입력
정수 a, b가 공백으로 구분되어 입력된다.(1<=a,b<=10,000)

출력
a, b의 최대공약수를 출력한다.

입력 예시
64 128

출력 예시
64


"""

import sys
input = lambda : sys.stdin.readline().rstrip()


def gcd(a, b):
    if a < b:
        a, b = b, a

    # b가 0이 될 때까지 반복
    while b:
        a, b = b, a % b

    return a


x, y = map(int, input().split())

# -- 내장 모듈로도 있음.
# from math import gcd
print(gcd(x,y))