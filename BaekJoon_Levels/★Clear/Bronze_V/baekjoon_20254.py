"""
ur 지역컨테스트 문제를 적어도 하나라도 푼 대학교 수 
tr 지역컨테스트 문제를 적어도 하나라도 푼 팀 수
uo TOPC 문제를 적어도 하나라도 푼 대학교 수 
to TOPC 문제를 적어도 하나라도 푼 팀 수


"""


import sys

input = sys.stdin.readline

ur, tr, uo, to = map(int, input().split())


print(56 * ur + 24 * tr + 14 * uo + 6 * to)
