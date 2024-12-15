import sys

input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())


def solve(a, b, c):
    if b >= c:
        return -1
    else:
        return int(a / (c - b) + 1)


print(solve(a, b, c))
