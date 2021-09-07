"""
1
7

Before

8
31

After

2
18

Special

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

m = int(input())
d = int(input())

if m < 2:
    print("Before")
elif m > 2:
    print("After")
elif m == 2 and 18 > d:
    print("Before")
elif m == 2 and 18 < d:
    print("After")
elif m == 2 and d == 18:
    print("Special")
