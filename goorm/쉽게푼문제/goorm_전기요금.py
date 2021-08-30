"""
100

0.70

193

1.35
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

consumption = int(input())

result = 0
if consumption < 100:
    result = consumption * 0.005
elif 100 <= consumption < 200:
    result = consumption * 0.007
elif 200 <= consumption < 300:
    result = consumption * 0.009
elif consumption >= 300:
    result = consumption * 0.01

print("%.2f" % result)
