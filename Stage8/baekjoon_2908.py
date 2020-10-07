# 734 893
# 437

import sys
input = sys.stdin.readline


a, b = input().split()
a = a[::-1]
b = b[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)
