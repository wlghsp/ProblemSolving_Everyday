


import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
a = [i for i in map(int, input().split())]
M = int(input())
b = [i for i in map(int, input().split())]
new = a + b
new.sort()
print(*new)