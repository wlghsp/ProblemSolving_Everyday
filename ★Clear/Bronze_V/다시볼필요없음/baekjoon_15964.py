import sys

input = sys.stdin.readline
""" 
4 3
7

3 4
-7
"""
a, b = map(int, input().split())

print((a + b) * (a - b))
