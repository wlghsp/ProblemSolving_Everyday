import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    sen = [i[::-1] for i in input().split()]
    print(*sen)