"""
4
-5 -2 7
5 -5 2
0 5 6
1 2 7

YES
NO
NO
YES

초기 위치는 (0,0)
로봇 청소기는 1초에 한 번 움직임, 상하좌우 하나의 방향으로 1의 거리를 움직임
이미 지나간 칸 재방문 가능 

N초의 시간이 흐른 뒤 (X,Y)에 위치 

"""
import sys

input = sys.stdin.readline

t = int(input())

cases = []
for _ in range(t):
    cases.append(list(map(int, input().split())))
