"""
현재 시각 
h hour
m min
s second

d 요리하는데 필요한 시간 (초)


"""


import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())
d = int(input())


print(h, m, s)
