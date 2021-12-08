"""
시작수(a)와 마지막 수(b)가 입력되면

a부터 b까지의 모든 홀수를 출력하시오.

입력
두 수 a, b 가 입력된다. (1<=a<=b<=100)

출력
a~b의 홀수를 모두 출력한다.

입력 예시
2 7

출력 예시
3 5 7

"""
import sys
input = lambda : sys.stdin.readline().rstrip()

def recur(start, end):
    if start % 2 != 0:
        print(start, end=" ")

    if start == end:
        return

    return recur(start+1, end)

a, b = map(int, input().split())

recur(a,b)



