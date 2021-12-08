"""
1부터 정수 n까지 출력하는 재귀함수를 설계하시오.
이 문제는 반복문 for, while 등을 이용하여 풀수 없습니다.
금지 키워드 : for while goto

입력
정수 n이 입력된다(1<=n<=200)

출력
1부터 n까지 한 줄에 하나씩 출력한다.
입력 예시
10

출력 예시
1
2
3
4
5
6
7
8
9
10
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

def recur(n):
    print(n)
    if n == k:
        return
    return recur(n+1)


k = int(input())
recur(1)