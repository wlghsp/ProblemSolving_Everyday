"""
팩토리얼(!)은 다음과 같이 정의된다.

n!=n×(n−1)×(n−2)×⋯×2×1

즉, 5!=5×4×3×2×1=120이다.

n이 입력되면 n!의 값을 출력하시오.

이 문제는 반복문 for, while 등을 이용하여 풀수 없습니다.

금지 키워드 : for while goto

입력
자연수 n이 입력된다. (n<=12)

출력
n!의 값을 출력한다.

입력 예시
5

출력 예시
120



"""


import sys
input = lambda : sys.stdin.readline().rstrip()


def f(n):
    if n <=1:
        return 1
    return n * f(n-1)


num = int(input())

print(f(num))