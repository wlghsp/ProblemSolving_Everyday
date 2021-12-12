"""




"""

import sys

input = lambda: sys.stdin.readline().rstrip()


n = int(input())


a = n % 8

if a == 1:
    print(1)
elif a in [0, 2]:
    print(2)
elif a in [7, 3]:
    print(3)
elif a in [6, 4]:
    print(4)
elif a == 5:
    print(5)
