import sys

input = sys.stdin.readline

n1, n2, n12 = map(int, input().split())


n = int((n1 + 1) * (n2 + 1) / (n12 + 1) - 1)
print(n)
