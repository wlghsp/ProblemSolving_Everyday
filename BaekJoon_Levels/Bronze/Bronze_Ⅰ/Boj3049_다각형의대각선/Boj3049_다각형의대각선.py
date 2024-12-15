import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

print(N * (N - 1) * (N - 2) * (N - 3) // 24)
