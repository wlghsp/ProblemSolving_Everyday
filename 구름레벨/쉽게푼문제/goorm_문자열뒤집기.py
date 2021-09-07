"""
1234567
7654321

string
gnirts
"""

import sys

input = sys.stdin.readline


literal = input().rstrip()

print(literal[::-1])
