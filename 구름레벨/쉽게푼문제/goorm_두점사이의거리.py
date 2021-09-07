"""
10 100
100 10

127.28

2 2
5 5

4.24


출력 소수점 2번째짜리까지 
"""


import sys

input = lambda: sys.stdin.readline().rstrip()

locs = []

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

distance= ((x2-x1)**2 + (y2 -y1)**2 ) ** 0.5

print("%.2f" % distance)