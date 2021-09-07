import sys

input = sys.stdin.readline

n, m = map(int, input().split())

line = True
left = False

for i in range(n):
    if line:
        for j in range(m):
            print("#", end="")
            line = False
        print()
    else:
        if left:
            print("#", end="")
        for j in range(m - 1):
            print(".", end="")
        if not left:
            print("#", end="")
        print()
        left = not left
        line = True
