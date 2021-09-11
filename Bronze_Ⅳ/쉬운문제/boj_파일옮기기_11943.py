"""
1 2
3 4

5


두 바구니의 최소값을 비교해서 

큰 

"""

import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
c, d = map(int, input().split())


c1 = a + d
c2 = c + b

if c1 > c2:
    print(c2)
else:
    print(c1)
