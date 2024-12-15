import sys
input = lambda : sys.stdin.readline().rstrip()

for i in range(int(input()), 0, -1):
    print("*" * i)