"""
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.


입력
입력으로 자연수 n이 입력된다. (1<=n<=10,000)

출력
1부터 n까지의 합을 출력한다.

입력 예시
100

출력 예시
5050


"""

import sys
input = lambda : sys.stdin.readline().rstrip()


def recur1(k):
    if k==1:
        return 1
    else:
        return recur(k-1) + k # O(n)


def recur(k):
    if k==1:
        return 1
    else:
        return 2 * recur(k//2) + ((k+1)//2) * ((k+1)//2) # O(lgn)

n = int(input())

print(recur(n))