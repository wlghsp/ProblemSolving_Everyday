import sys

input = sys.stdin.readline
""" 
11 15
19

4 3
2

R1 과 R2 두 수의 평균 S
S = (R1 + R2)/2

입력 
정수 R1과 S

출력
R2 출력
"""
r1, s = map(int, input().split())

r2 = 2 * s - r1
print(r2)
