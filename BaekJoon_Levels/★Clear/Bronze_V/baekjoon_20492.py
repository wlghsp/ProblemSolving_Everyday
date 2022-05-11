import sys

input = sys.stdin.readline


num = int(input())

a = int(num - (num * 0.22))
b = int(num - (num * 0.2 * 0.22))
print(a, b)
