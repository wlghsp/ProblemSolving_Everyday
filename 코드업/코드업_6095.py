"""
5
1 1
2 2
3 3
4 4
5 5



"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
baduk = [[0] * 19 for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    baduk[x - 1][y - 1] = 1

for row in baduk:
    print(*row)
