"""
두 수를 거꾸로 출력하기..
세 수를 거꾸로 출력하기...
이런 문제들은 쉽게 풀 수 있었다.
이번에는 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 데이터의 개수 n이 입력된다. ( n <= 1,000 )
둘째 줄에 공백을 기준으로 n개 데이터가 입력된다.

출력
n개의 데이터를 입력의 역순으로 출력한다.

입력 예시
5
1 3 5 6 8

출력 예시
8 6 5 3 1


"""

import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
stack = list(map(int, input().split()))

for i in range(len(stack)):
    print(stack.pop(), end=" ")



