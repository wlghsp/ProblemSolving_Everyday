import sys
input = lambda : sys.stdin.readline().rstrip()


a, b, c = map(int, input().split())


ba = b - a - 1
cb = c - b - 1

print(ba if ba > cb else cb)