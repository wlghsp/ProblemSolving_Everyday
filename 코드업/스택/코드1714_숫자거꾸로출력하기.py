'''
현우는 숫자를 좋아한다. 항상 숫자를 가지고 장난을 하고 숫자로 무언가 만들기를 취미생활로 즐기고 있다.
하루는 어떤 숫자를 쓰고, 그 수를 거꾸로 쓰기로 했다.
어떤 수 N이 입력되면 그 수를 거꾸로 출력하는 프로그램을 작성하시오.
예)
입력 : 2571
출력 : 1752
입력 : 1200
출력 : 0021

입력
입력되는 수 N은 0이상의 정수이다.

출력
입력된 수를 거꾸로 출력한다.

입력 예시
123456

출력 예시
654321



'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = input()

stack = list(n)

for _ in range(len(stack)):
    print(stack.pop(), end="")


