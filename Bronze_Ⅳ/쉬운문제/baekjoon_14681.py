"""
12
5

1

9
-13

4

"""
import sys

input = sys.stdin.readline

x = int(input())
y = int(input())
quadrant = 0

if x > 0 and y > 0:
    quadrant = 1
elif x > 0 and y < 0:
    quadrant = 4
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
print(quadrant)
