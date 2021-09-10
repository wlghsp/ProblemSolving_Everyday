"""
2003 3 5
2003 4 5

0
1
0

만 나이
세는 나이
연 나이

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

y, m, d = map(int, input().split())
dy, dm, dd = map(int, input().split())
