"""
1
10
12
13

Fish Rising

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

depth = []
for _ in range(4):
    depth.append(int(input()))

isIdentical_set = len(set(depth))
result = ""
if isIdentical_set == 1:
    result = "Fish At Constant Depth"
else:
    if depth[0] > depth[1] > depth[2] > depth[3]:
        result = "Fish Diving"
    elif depth[0] < depth[1] < depth[2] < depth[3]:
        result = "Fish Rising"
    else:
        result = "No Fish"

print(result)
