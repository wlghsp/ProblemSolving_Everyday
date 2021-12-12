"""
1 2

1

1 3

1

2 2

2
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
print(n * m // 2)
