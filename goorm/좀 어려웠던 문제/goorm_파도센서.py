"""
-1 0 1
2 2
-2 -2
0 0
-1 -2
1 2

3

-9 -2 10
9 -5
8 1-
-5 -9
2 4
-5 9

3
"""
import sys
input = sys.stdin.readline

x, y, r = map(int, input().split())

locations = []
for i in range(5):
    locations.append(list(map(int, input().split())))

distances = []
for i, loc in enumerate(locations):
    a = loc[0] - x
    b = loc[1] - y
    dist = ((a**2) + (b**2))**(1/2)
    distances.append(dist)

if r >= min(distances):
    print(distances.index(min(distances)) + 1)
else:
    print(-1)