
"""
어떤 10진수 n이 주어지면 2진수로 변환해서 출력하시오.

예)

10    ----->  1010
0    ----->  0
1    ----->  1
2    ----->  10
1024    ----->  10000000000

이 문제는 반복문을 이용하여 풀 수 없습니다.
금지 키워드 : for while goto

입력
10진수 정수 n이 입력된다.
(0<=n<=2,100,000,000)

출력
2진수로 변환해서 출력한다.

입력 예시
7

출력 예시
111

"""

import sys
input = lambda : sys.stdin.readline().rstrip()


def toBin(n):
    if n == 0 or n == 1:
        return n
    else:
        toBin(n//2)
        print(n%2, end='')
    return 0

num = int(input())

toBin(num)