"""
조금 어려웠던 문제 답 보고 풀었음 

수식을 손으로 적고 정리해서 판매량을 구하는 식 도출 적용

"""

import sys

input = sys.stdin.readline

# A 고정비용, B 가변 비용, C 노트북 가격

A, B, C = map(int, input().split())

# 가변비용이 노트북 가격보다 크거나 같으면 이익을 낼 수 없어 손익분기점 도출 불가
if B >= C:
    print(-1)
else:
    print(int(A / (C - B)) + 1)
