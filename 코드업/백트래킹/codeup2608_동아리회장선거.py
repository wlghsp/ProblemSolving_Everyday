

'''
정보 동아리 회장을 선출하려고 한다.
올해는 단일 후보만 등록하여 찬반 투표를 실시하였다.
n명의 학생이 O, X로 의사 표현을 한다면 나올 수 있는 경우를 모두 출력하시오.
예를 들어 2명이 투표하는 경우 나올 수 있는 경우는

OO

OX

XO

XX

이다.

입력
투표자 수 n이 정수로 입력된다.(1 <= n <= 7)

출력
나올 수 있는 모든 경우의 수를 출력한다.
찬성은 알파벳 대문자 O, 반대는 알파벳 대문자 X로 표시한다.

입력 예시
3

출력 예시
OOO
OOX
OXO
OXX
XOO
XOX
XXO
XXX


'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(now):
    if now == n:
        print(''.join(ans))
        return
    ans[now] = 'O'
    dfs(now + 1)
    ans[now] = 'X'
    dfs(now + 1)


n = int(input())
ans = ["" for _ in range(n)]

dfs(0)