
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

for i in range(1, N+1):
    line = '*' * i
    print(line)