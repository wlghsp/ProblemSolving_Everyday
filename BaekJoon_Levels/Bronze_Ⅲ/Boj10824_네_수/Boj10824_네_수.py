
import sys
input = lambda : sys.stdin.readline().rstrip()

a, b, c, d = input().split()

first = int(a + b)
second = int(c + d)
print(first + second)
