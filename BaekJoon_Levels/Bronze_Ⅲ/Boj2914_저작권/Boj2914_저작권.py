import sys
input = lambda: sys.stdin.readline().rstrip()
a, i = map(int, input().split())

print(((i-1) * a) + 1)