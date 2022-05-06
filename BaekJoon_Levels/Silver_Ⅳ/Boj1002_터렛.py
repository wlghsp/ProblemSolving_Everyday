"""
두 원 사이의 접점의 갯수를 묻는 문제
https://itstory1592.tistory.com/33 여기 설명이 다 있다.
"""

import sys, math

input = lambda : sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 점의 거리 원의 방정식
    if distance == 0 and r1 == r2: # 두 원의 크기가 같은 경우 접점이 무수히 많다.
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance: # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2): # 두 원이 서로 다른 두 점에 서 만날 때
        print(2)
    else:
        print(0) # 그외에


