"""
5
1 9 29 59 60

1

10
20 90 130 450 923 1020 2943 3920 9431 11309

40
"""


import sys

input = lambda: sys.stdin.readline().rstrip()


n = int(input())


dots = list(map(int, input().split()))


min_distance = 999999
for i in range(len(dots) - 1):
    gap = dots[i + 1] - dots[i]
    if gap < min_distance:
        min_distance = gap

print(min_distance)
