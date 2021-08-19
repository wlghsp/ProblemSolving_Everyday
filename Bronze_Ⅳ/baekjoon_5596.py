"""
100 80 70 60
80 70 80 90

100 80 70 60
80 70 60 100
"""
import sys

input = sys.stdin.readline

sum1 = sum(list(map(int, input().split())))
sum2 = sum(list(map(int, input().split())))

if sum1 >= sum2:
    print(sum1)
elif sum1 < sum2:
    print(sum2)
