"""
100000 5.5 5

130696.00

5550000 2.3 2

5808235.95
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

principal, interest, duration = map(int, input().split())
