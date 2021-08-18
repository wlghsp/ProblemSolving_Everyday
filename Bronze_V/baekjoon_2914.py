import sys

input = sys.stdin.readline
""" 
입력
38 24

출력
875



"""
a, i = map(int, input().split())

print((i - 1) * a + 1)
