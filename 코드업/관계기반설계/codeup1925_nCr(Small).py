
"""
nCr은 n개의 원소를 가지는 집합에서 r개의 부분 집합을 고르는 조합의 수를 말한다.

입력
n과 r이 입력된다. (1<=r<=n<=30)

출력
nCr의 값을 출력한다.

입력 예시
5 2

출력 예시
10


"""

import sys
input = lambda : sys.stdin.readline().rstrip()


# 팩토리얼
def f(n):
    if n <=1:
        return 1
    return n * f(n-1)


# combination 공식
# result = f(n) // (f(n-r) * f(r))
# https://ansohxxn.github.io/algorithm/combination/
def combination(n,r):
    if n==r or r==0: # 재귀 탈출 조건 n== r 이나 r== 0이면 1이다.
        return 1
    else:
        # nCr = n-1Cr-1 + n-1Cr
        return combination(n-1, r-1) + combination(n-1, r)

a, b = map(int, input().split())
print(combination(a,b))